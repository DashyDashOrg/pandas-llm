const {expect} = require('@playwright/test') 


exports.SignIn = class SignIn
{
    constructor(page)
    {
        this.page = page
        this.email = page.locator('[formcontrolname="userEmail"]')
        this.password = page.locator('[formcontrolname="userPassword"]')
        this.login = page.getByRole('Button', {name: 'Login'})
    }


    async GoTo_LoginPage()
    {
        await this.page.goto('https://rahulshettyacademy.com/client')
    }
    async Login()
    {
        await this.email.fill('test_1@gmail.com')
        await this.password.fill('Test@123')
        await this.login.click()
    }

}