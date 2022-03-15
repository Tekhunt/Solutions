import Header from '../components/LoginComponents/Header'
import Login from '../components/LoginComponents/Login'
import Image from '../components/LoginComponents/Image'


function LoginPage() {
    return (
        <div class="login-app">
            <Header />
            <div className="inner-container">
                <div className="laptop-img">
                <Image url="https://res.cloudinary.com/decagonbouncer/image/upload/v1576756310/bouncer-frontend/jonh_sv_vrsxva.svg" />
                </div>
                <div className="right-container">
                    <Login />  
                </div> 
            </div>
        </div>
    )
}

export default LoginPage