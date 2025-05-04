import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import WebDriverException

def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="Browser to run tests: chrome, firefox, or edge"
    )
    parser.addoption(
        "--headless", 
        action="store_true", 
        default=False, 
        help="Run browser in headless mode"
    )
    parser.addoption(
        "--implicit-wait", 
        action="store", 
        default=5, 
        type=int, 
        help="Implicit wait time in seconds"
    )
    parser.addoption(
        "--base-url", 
        action="store", 
        default="https://stellarburgers.nomoreparties.site", 
        help="Base URL for the application"
    )

@pytest.fixture(scope="session")
def config(request):
    return {
        "browser": request.config.getoption("--browser"),
        "headless": request.config.getoption("--headless"),
        "implicit_wait": request.config.getoption("--implicit-wait"),
        "base_url": request.config.getoption("--base-url")
    }

@pytest.fixture
def driver(request, config):
    browser = config["browser"].lower()
    headless = config["headless"]
    implicit_wait = config["implicit_wait"]
    
    
    try:
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--start-maximized")
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
        driver.implicitly_wait(implicit_wait)
        
        test_name = request.node.name
        
        yield driver
        
    except WebDriverException as e:
        raise
    finally:
        if 'driver' in locals():
            driver.quit()

@pytest.fixture
def base_url(config):
    return config["base_url"]

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        try:
            driver = item.funcargs.get("driver")
            if driver:
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                screenshot_dir = "screenshots"
                if not os.path.exists(screenshot_dir):
                    os.makedirs(screenshot_dir)
                screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")
                driver.save_screenshot(screenshot_path)
        except Exception:
            pass
