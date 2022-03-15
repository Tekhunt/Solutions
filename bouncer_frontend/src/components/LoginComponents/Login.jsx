import React from 'react';
import {useState, useEffect} from 'react';
import InputField from './InputField';
import Caption from './Caption';
import PasswordField from './PasswordField';
import SignUpButton from './SignUpButton';
import axios from "axios";
import { useHistory } from 'react-router';
import { toast } from 'react-toastify';



const baseURL = "https://bouncerb.herokuapp.com/api/v1/login/";

function Login(){
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const history = useHistory();
    const [redirects, setRedirects]=useState(false);
    const [error, setError] = useState(null)

    useEffect(()=>{

        if (redirects){
            history.push("/")
        }
    },[redirects, history])

    function handleUsername(e){
        setEmail(e.target.value)
      }
    
    function handlePassword(e){
    setPassword(e.target.value)
    }

    
    
    const handleSubmit = (e) =>{
    
        const data = {
            email: email,
            password: password,
        }
        e.preventDefault();

        const config={
            header:{
                'Content-Type': 'application/json'
            }

        }
        axios
        .post(baseURL, data, config)
        .then(res => {
        setRedirects(true)
            
    }, err=>{
        if(err.res.status === 400){
            toast("This User is not Registered", {type:"error"})
        }
    })
        .catch((err) =>{ console.log('Axios Error',err);
    setError(error);
    toast("Invalid credentials", {type:"error"})
    })

    }
    // if (!email || !password) return "No post!"
    return (
        <div>
            <form  className="form-components" onSubmit={e => handleSubmit(e)}>
                <Caption left="Sign in" leftUrl="login" right="Register" idleft="id" rightUrl="register" />
            
                <InputField label="Username" type="text" value={email} change={e => handleUsername(e)} />
                <PasswordField label="Password" type="password" value={password} change={e => handlePassword(e)}  />
                <SignUpButton action="Login" type="submit"/>
            
                <Caption left="Become a vendor" leftUrl="vendor" right="Forgot password" rightUrl="forgotpassword" />
            </form>
        </div>
    )
}

export default Login;