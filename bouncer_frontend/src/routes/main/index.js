import { Suspense } from 'react'
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import MyLoader from '../../utils/loader'
import {ToastContainer} from "react-toastify"
import 'react-toastify/dist/ReactToastify.css'
import ForgotPassword from '../../components/ForgetPassword/forgetPassword'
import HomePage from '../../pages/HomePage'
import LoginPage from '../../pages/LoginPage'
import Register from '../../pages/RegisterPage'


const App = () => (
  <Suspense fallback={ 
    <div>
      <MyLoader /> 
    </div>
  }>


  <Router>

    <div className="App">
        <ToastContainer/>


          <Switch>
            <Route path="/forgot-password" component={ForgotPassword}/>
            <Route exact path='/' component={HomePage} />
            <Route exact path="/login" component={LoginPage} />
            <Route path="/register" component={Register} exact />
          </Switch>
      </div>
    
   </Router>

  </Suspense>
)

export default App;