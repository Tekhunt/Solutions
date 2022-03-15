import styled from "styled-components";

export const Wrapper = styled.div`
  font-family: 'Open Sans', sans-serif;
  margin: 2% 15% 2% 15%;

  
.logo {
    color: #ef6e7b;
    font-size: 2rem;

}
  
.eye{
  color: dodgerblue;
  padding-right: 7px;
}
.passEye{
  display:flex;
  justify-content: space-between;
}
  
  .container {
    color: black;
    display: flex;
    gap: 50px;
    justify-content: center;
    align-items: flex-start;
    width: 100%;
  }
  .img {
    padding-top: 20px; 
    width: 100%;
  }
  
  .reg-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 50px;
  }

  .sign {
    font-weight: 400;
    background-color: transparent;
    cursor: pointer;
    border: none;
    &:hover {
      color: #ef6e7b;
    }
  }

  .pass{
    font-weight: 400;
    background-color: transparent;
    cursor: pointer;
    border: none;
    &:hover {
      color: #ef6e7b;
    }
  }

  .reg {
    font-weight: 400;
    border-bottom: 3px solid #ef6e7b;
    background-color: transparent;
    cursor: pointer;
    border-top: none;
    border-right: none;
    border-left: none;
    &:hover {
      color: #ef6e7b;
    }
  }
  
  .button {
    color: #ffffff;
    background-color: #ed4856;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 6.8vh;
    width: 32vw;
    margin-top: 5%;
  }
  .footer {
    display: flex;
    justify-content: space-between;
    font-size: 17px;

  }

  input {
    font-family: 'Open Sans', sans-serif;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    width: 32vw;
    height: 5vh;
    border-radius: 5px;
    border: 3px solid #f9fafb;
    background-color: transparent;
    padding-left: 1rem;
    margin: 0.5rem 0;
  }

} 

  @media only screen and (max-width: 767px) {

    .header {
      margin-top: 70px;
      display: flex;
      justify-content: center;
    }

    
    .image{
      display:none;
    }
    .img{
      display:none;
    }

    .form {
      width: 100%;
    }

     .dinput {
      width: 90%;
    } 
    .button{
      width: 100%;
    }  

  

`;

export const Input = styled.input`
  font-family: 'Open Sans', sans-serif;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: 29vw;
  height: 5vh;
  border-radius: 5px;
  border: 3px solid #f9fafb;
  background-color: transparent;
  padding-left: 1rem;
  margin: 0.5rem 0;

 

`;

