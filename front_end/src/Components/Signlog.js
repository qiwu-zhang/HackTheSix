import React, {useState, useReducer} from "react";
import ScriptTag from "react-script-tag";
import Dashboard from "./dashboard/Dashboard";
import {useLocation, useRouteMatch, useHistory} from "react-router-dom";
import { v4 as uuid } from "uuid";
import "../static/main.css";
import "./Signlog.scss";
const BASE_URL = "http://localhost:3000";
let id = uuid(); // unique id will be updated when logged out
const errorReducer = function reducer(state, action) {
    switch (action.type) {
      case 'DOES NOT EXIST':
        return {type : "Either your username or password is wrong"};
      case 'FORGETFUL':
        return {type: "Did you eat your password?"};
      case "":
        return {type: ""};
    }
}


export default () => {
    let history = useHistory()
    let location = useLocation();
    let match = useRouteMatch("/" + (id + []));
    console.log(location);
    console.log(history)
    console.log(match);
    const [RPanel, setRPanel] = useState(false);
    const [submit, setSubmit] = useState(false);
    const [loginSubmit, setLoginSubmit] = useState(false);
    const [registerSubmit, setRegisterSubmit] = useState(false);
    const [errorState, dispatch] = useReducer(errorReducer, {type : ""}); 
    const [registerForm, setRegisterForm] = useState({});
    const [loginForm, setLoginForm] = useState({});
    const [numFails, setNumFails] = useState(0);
    const submitHandling = async function submit(e) {
        e.preventDefault();
        let formData = new FormData();
        let pathName = e.target.name;
        let form = (pathName === "login") ? loginForm : registerForm; 
        if (pathName === "login"){
            setLoginSubmit(true);
            setRegisterSubmit(false);
        } else {
            setLoginSubmit(false);
            setRegisterSubmit(true);
        }

        for(let key of Object.keys(form)){
            formData.append(key, form[key]);
        } // for

        console.log(form);
    
        let path = "/" + pathName;
        await fetch(path, {
            method: "POST",
            "Content-Type" : "multipart/form-data;charset=utf-8",
            body : formData
        }).then(response => {
            if (response.status === 200) {
                alert("Post successful");
                return response.text();
            } else {
                alert("Post unsuccessful, ERROR " + response.status);
            }
        }).then(data => {
            alert(data);
            if (data === "Login Unsuccessful"){
                dispatch({type : "DOES NOT EXIST"});
                setNumFails(numFails + 1);
                alert(numFails);
                if (numFails >= 5) {
                    dispatch({type : "FORGETFUL"});
                    setNumFails(0);   
                }
            } else if (data === "Login Successful"){
                dispatch({type : ""})
                history.push(id);
            }
        }).catch(err => alert(err));
    }
    
    const signInChange = (e) => {
        console.log(e);
        let name = e.target.name;
        let value = e.target.value;
    
        setLoginForm(prevState => ({
            ...prevState,
            [name] : [value]
        }));
    }
    
    const signUpChange = (e) => {
        let name = e.target.name;
        let value = e.target.value;
        
        setRegisterForm(prevState => ({
            ...prevState,
            [name] : [value]
        }));
    }

    if (match && match.isExact){
      return (<Dashboard/>);
    }
    

    return(
    <React.Fragment>
    <div className={`container + ${RPanel && "right-panel-active"}`} id="container">
        <div className="form-container sign-up-container">
          <form onSubmit={submitHandling} name="register">
            <h1>Create Account</h1>
            <input type="text" name="name" placeholder="Name" onChange={signUpChange} required />
            <input type="email" name="email" placeholder="Email" onChange={signUpChange} required />
            <input type="text" name="password" placeholder="password"onChange={signUpChange} required />
                <small style={{color : "red"}}>{registerSubmit && errorState.type}</small>
            <button type="submit">SignUp</button>
          </form>
        </div>
        <div className="form-container sign-in-container">
          <form onSubmit={submitHandling} name="login">
            <h1>Sign In</h1>
            <input type="email" name="email" placeholder="Email" onChange={signInChange} required />
            <input type="password" name="password" placeholder="password" onChange={signInChange} required />
            <a href="forgot-password.html">Forgot Your Password?</a>
                <small style={{color : "red"}}>{loginSubmit && errorState.type}</small>
            <button type="submit"> SignIn</button>
          </form>
        </div>
        <div className="overlay-container">
          <div className="overlay">
            <div className="overlay-panel overlay-left">
              <h1>Welcome Back!</h1>
              <p>To keep connected with us please login with your personal info</p>
              <button className="ghost" id="signIn" onClick={(e) => { setRPanel(false) }}>Sign In</button>
            </div>
            <div className="overlay-panel overlay-right">
              <h1>Hello, Friend!</h1>
              <p>Enter your personal details and start journey with us</p>
              <button className="ghost" id="signUp" onClick={(e) => { setRPanel(true) }}>Sign Up</button>
            </div>
          </div>
        </div>
      </div>
      </React.Fragment>
     );
};