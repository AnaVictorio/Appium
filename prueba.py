#importo la libreria de webdriver desde el folder de appium
from appium import webdriver
from selenium.webdriver.common.by import By

#seteo los valores con los cuales voy a establecer la conexion ak dispositivo, en este caso abriendo la app de figma
desiredCap = {
    "deviceName": "Pixel 2 API 29 2",
    "platformName": "Android",
    "appPackage": "com.google.android.apps.nexuslauncher",
    "appActivity": "com.google.android.apps.nexuslauncher.NexusLauncherActivity"
}
#establezco la ruta del webdriver junto con los valores iniciales definidos anteriormente
driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredCap)

#realizo log in en Figma
driver.implicitly_wait(10)
driver.find_element(By.ID, 'com.google.android.apps.nexuslauncher:id/search_container_all_apps').click()
