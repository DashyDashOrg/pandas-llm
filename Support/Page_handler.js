const {SignUp} = require('./Page_Object/SignupPage')
const {SignIn} = require('../Support/Page_Object/SignInPage')
const {OrderProduct} = require('../Support/Page_Object/OrderProduct')
const {OrderVerify} = require('../Support/Page_Object/OrderVerify')
exports.Object = class Object
{
    constructor(page)
    {
        this.page = page
        this.signup = new SignUp(this.page)
        this.signIn = new SignIn(this.page)
        this.order = new OrderProduct(this.page)
        this.verifyOrder = new OrderVerify(this.page)
    }

   getSignUp()
   {
    return this.signup
   }
   getSignIn()
   {
    return this.signIn
   } 
   getOrder()
   {
    return this.order
   }
   getVerifyOrder()
   {
    return this.verifyOrder
   }
 
}
