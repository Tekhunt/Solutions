import Laptop from './laptop';
import NavBar from './navBar';
import './styles/forget.css';


const ForgotPassword = () => {
    
    return (
        <div className="main-container">
           <div className="nav">
               <a href="https://bouncerapp.netlify.app/"> <NavBar/> </a>
           </div>
            <div className="main">
                <Laptop/>
                <div className='sub-main'>
                    <div className="heading">
                    <div>
                        <p className="forgot" >Forgot Password</p>
                        <p className="password-in-line"></p>
                    </div>
                    </div>
                    <div className="username">
                        
                        <form>    

                            <label For="text" >Email:</label><br/>
                            <input type="email"  name="email" autoFocus/><br/>
                            <input type="submit" name ="submit1" value="Submit"/>

                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default ForgotPassword;
