const {expect, request}  = require('@playwright/test')

exports.API_call = class API_call
{ 
    constructor(apiContext,loginPayload) // api context pass in the actual test
    {
        this.apiContext = apiContext
        this.loginPayload = loginPayload
          
    }




    async getToken()
    {
        const loginResponse = await this.apiContext.post('https://rahulshettyacademy.com/api/ecom/auth/login', 
        {
           data: this.loginPayload
        })


        const loginResponseJson = await loginResponse.json()

        expect(loginResponse.ok()).toBeTruthy()
        let token = loginResponseJson.token
        return token
    }


    async createOrder(OrderPayload)
    {
        
   const CreateOrderResponse = await this.apiContext.post('https://rahulshettyacademy.com/api/ecom/order/create-order',
       {
         data: OrderPayload,
         headers:  {
                    'Authorization' : await this.getToken(),
                    'Content-Type' : 'application/json'
                   }
      })

           const OrderResponseJson = await CreateOrderResponse.json()
           const orderID = OrderResponseJson.orders[0]
           return orderID
    }



    async AddTokenInLocalStorage(page)
    {
        page.addInitScript(value => {

            window.localStorage.setItem('token',value);
        }, await this.getToken() );
    }
}