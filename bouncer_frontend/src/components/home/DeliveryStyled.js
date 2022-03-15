import styled from 'styled-components';

export const DeliveryWrapper = styled.section`
        max-width: 1200px;
        margin: 0px auto;
        padding: 0 2rem; 
    .delivery{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        justify-self: center;
        grid-column-gap: 50px;
    }

    .delivery .delivery-icon{
        display: flex;
        justify-content: center;
    }

    .delivery div div > img{
        margin: 100px 0 0 0;
    }
    .delivery div > h1{
        font-size: 1.5rem;
        margin: 30px 0;
        text-align: center;
    }
    .delivery div > p{
        font-weight: 300;
        text-align:start;
    }

    @media only screen and (max-width: 767px){
        .delivery{
            display: grid;
            grid-template-columns: 1fr;
            justify-self: center;
        }
    }
    
`