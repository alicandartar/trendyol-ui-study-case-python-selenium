from selenium.webdriver.common.by import By

class Locators():
    baseURL = "https://trendyol.com"
    
    accountButton = (By.CSS_SELECTOR , "#account-navigation-container > div > div.account-nav-item.user-login-container")
    accountLoginButton = (By.CSS_SELECTOR,"#account-navigation-container > div > div.account-nav-item.user-login-container > div.login-dropdown > div > div.login-button")
    popupCloseButton = (By.CSS_SELECTOR,"html.fancybox-margin.fancybox-lock body div.fancybox-overlay.fancybox-overlay-fixed div.fancybox-wrap.fancybox-desktop.fancybox-type-html.fancybox-opened div.fancybox-skin a.fancybox-item.fancybox-close")

    emailTextBox = (By.ID, "login-email")
    passwordTextBox = (By.ID,"login-password-input")
    loginButton = (By.CSS_SELECTOR,"#login-register > div.lr-container > div.q-layout.login > form > button")

    firstButique = (By.CSS_SELECTOR,"#navigation-wrapper > nav > ul > li:nth-child(1)")
    choosedStore = (By.CSS_SELECTOR, "#browsing-gw-homepage > div > div:nth-child(2) > div.sticky-wrapper > div.component-list.component-big-list > article:nth-child(1)")
    chooseProduct = (By.CSS_SELECTOR, "#search-app > div > div > div.srch-prdcts-cntnr > div:nth-child(2) > div > div:nth-child(2) > div.p-card-chldrn-cntnr > a > div.image-container > div > img")
    addToBasketButton = (By.CSS_SELECTOR,".add-to-bs")
    

   