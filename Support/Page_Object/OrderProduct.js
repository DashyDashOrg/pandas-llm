const {expect} = require('@playwright/test')
import * as productData from "../testData/productData.json"


exports.OrderProduct = class OrderProduct
{
    constructor(page,isMobile)
    {
        this.isMobile = isMobile
        this.page = page
        this.hamburgerIcon = page.locator("label.hamberger-btn")
        this.product = page.locator('.card-body')
        this.product_name = productData.productName
        this.cart = page.locator('[routerlink="/dashboard/cart"]')
        this.checkout = page.getByRole('button',{name:'Checkout'})
        this.toastConfirmation = page.locator("[aria-label='Product Added To Cart']")
        
        
    }

    async ProductAddToCart()
    {
        let productCount = await this.product.count()
        console.log(productCount)


        for (let i=0;i<3; i++)
        {
            var productsearch = await this.product.locator('b').nth(i).textContent()
            console.log(productsearch)
            if (await productsearch == this.product_name)
          {
            this.product.locator('text= Add To Cart').nth(i).click()
            await this.toastConfirmation.waitFor({state:"visible"})
            await expect(this.toastConfirmation).toHaveText(productData.productAddedToastMessage)
            await this.page.waitForLoadState('networkidle')
            break
          }

        }
        
    }


    async CheckoutProduct()
    {
        if (this.isMobile) {
            await this.hamburgerIcon.click()
        }
        await this.cart.waitFor({state:"visible"})
        await this.cart.click()
        await expect(this.page).toHaveURL('https://rahulshettyacademy.com/client/dashboard/cart')
        await this.checkout.waitFor({state:"visible"})
        await this.checkout.click()

    }
}