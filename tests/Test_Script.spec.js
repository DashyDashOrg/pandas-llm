
const {test} = require('../Support/Fixture/Page_Object_fixture')
const OrderPayload = { orders: [{ country: "India", productOrderedId: "6262e990e26b7e1a10e89bfa" }] }


/**
 * This test is for Login and creating order automation work flow
 */
test('Login and create order', async({API,VerifyOrder,loginPage }) => 
{
    
    await test.step('Place the order', async() => 
    {
        const OrderID = await API.createOrder(OrderPayload)

        await loginPage.GoTo_LoginPage()
        await VerifyOrder.orderVerify(OrderID)
        
    });

})


/**
 * This test is for End to End web application process
 */
test('Verify End to end testing', async ({ registerPage,loginPage,orderSelectedProduct}) => 
{
  
    /**
     * This is Sign up functionality workflow
     */
    await test.step('Signup functionality', async () => {

        await registerPage.GoTo()
        await registerPage.getLabel()
        await registerPage.getInputValue()

    })

    /**
     * This is Login functionality workflow
     */
    await test.step('login functionality', async () => {
        await loginPage.GoTo_LoginPage()
        await loginPage.Login()
    })

    /**
     * This is Create Order functionality workflow
     */
    await test.step('Create Order', async () => {
        await orderSelectedProduct.ProductAddToCart()
        await orderSelectedProduct.CheckoutProduct()
    })

})