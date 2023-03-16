const {expect} = require('@playwright/test')



exports.OrderProduct = class OrderProduct
{
    constructor(page)
    {
        this.page = page
        this.product = page.locator('.card-body')
        this.product_name = 'adidas original'
        this.cart = page.locator('[routerlink="/dashboard/cart"]')
        this.checkout = page.getByRole('button',{name:'Checkout'})
        
        
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
            await this.page.waitForLoadState('networkidle')
            break
          }

        }
        
    }


    async CheckoutProduct()
    {
        await this.cart.click()
        await expect(this.page).toHaveURL('https://rahulshettyacademy.com/client/dashboard/cart')
        await this.checkout.click()

    }
}