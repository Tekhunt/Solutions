import styled from 'styled-components';

export const ItemWrapper = styled.section`

    .best-seller {
        display: flex;
        justify-content: center;
        margin: 50px 0;
        font-size: 1.875rem;
        font-weight: 600;
    }

    .menu-bar{
        max-width: 700px;
        margin: 0px auto;
    }
    .menu-bar ul{
        display: flex;
        justify-content: space-evenly;
        margin-top: 70px;
        flex-wrap: wrap;
    }
    .menu-bar li{
        list-style: none;
    }
    .menu-bar a{
        color: black;
        text-decoration: none;
        cursor: pointer;
        font-weight: 400;
    }
    .menu-bar ul a:hover{
    border-bottom: 4px solid #33A0FF;
    padding-bottom: 10px;
}
`