from selenium import webdriver
capabilities = webdriver.DesiredCapabilities.EDGE.copy()
capabilities["extensionPaths"] = ["C:\\Users\\automation\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\LocalState\\Extensions\\MyExtn"]
# Tried with this path too "C:\\Users\\automation\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\LocalState\\MyExtn"
edge = webdriver.Edge(executable_path="C:\\Users\\automation\\Documents\\ashok_mb_mac_zen\\Automation\\Frameworks\\Selenium\\MicrosoftWebDriver.exe", capabilities=capabilities)