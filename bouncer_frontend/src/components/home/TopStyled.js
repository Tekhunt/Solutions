import styled from 'styled-components';

export const NavWrapper = styled.section`
    background-color: #F6F7F8;
    > header {
        max-width: 1200px;
        margin: 0px auto;
        padding: 0 2rem; 
    }

    > header > div{
        display:flex;
        justify-content: space-between;
        align-items: center;
        height: 50px;
        font-size: 0.875rem;
        flex-wrap: wrap;
    }
    @media only screen and (max-width: 767px){
        background-color: #F6F7F8;
        height: 70px;
    }
`
export const SelectLang = styled.select`
    border: 2px solid #FFFFFF;
    padding: 8px 7px;
    border-radius: 4px;
    background-color:#F6F7F8;    

`
export const SelectSpace = styled.span`
    padding: 8px 4px;
`

export const UserSection = styled.div`

    .user-profile{
    padding-right: 16px;
    text-decoration: none;
    color: black;
    }
    .profile-section > i{
        margin-right: 7px;
    }
    .basket-shopping{
    padding-right: 5px;
    }
    .search{
        padding-left: 18px;
    }
    .amount-cart{
        color: #b4b5b6;
        margin-left: 5px;
    }
    .fas {
        color: black;
    }
`