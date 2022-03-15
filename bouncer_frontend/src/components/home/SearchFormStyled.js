
import styled from 'styled-components';

export const FormWrapper = styled.section`
    max-width: 1200px;
    margin:  auto;
    padding: 0 2rem;
    .input-product{
        display: flex;
        justify-content: center;
        margin: 150px 0;
    }
    input[type=text]{
        padding: 15px 10px;
        width: 50%;
        outline: none;
        border: 2px solid rgb(241, 243, 244);
        font-size: 18px;
    }
    input[type=submit]{
        background-color: #33A0FF;
        color: white;
        width: 100px;
        border:none;
        font-size: 1rem;
        cursor: pointer;
        padding: 15px 30px;
    }
`
