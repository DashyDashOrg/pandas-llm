const {expect} = require('@playwright/test') 
import * as loginData from "../testData/loginTestdata.json"


exports.SignIn = class SignIn
{
    constructor(page, isMobile)
    {
        this.page = page
        this.isMobile = isMobile
        this.confiramtionToast = page.locator("[aria-label='Login Successfully']")
        this.email = page.locator('[formcontrolname="userEmail"]')
        this.password = page.locator('[formcontrolname="userPassword"]')
        this.login = page.getByRole('Button', {name: 'Login'})
    }


    async GoTo_LoginPage()
    {
        await this.page.goto(loginData.baseURL)
    }
    async Login()
    {
        await this.email.fill(loginData.email)
        await this.password.fill(loginData.password)
        await this.login.click()
        await this.confiramtionToast.waitFor({state:"visible"})
        await expect(this.confiramtionToast).toHaveText(loginData.loginSuccesfullyToastMessage)
        await this.confiramtionToast.waitFor({state:"hidden"})
    }

}