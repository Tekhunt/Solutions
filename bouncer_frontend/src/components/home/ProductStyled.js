import styled from 'styled-components';

export const ProductWrapper = styled.section`
    .container-card{
        max-width: 1000px;
        margin: 0px auto;
        padding: 0 2rem; 
    }
    .laptop-card{
        border: 4px solid #F6F7F8;
        padding: 25px;
        margin: 20px 0;
    }
    .laptop-card > div > img{
        width: 100%;
    }
    .laptop-card div >h3{
        margin-top: 20px;
        text-align: center;
    }
    .laptop-card .star-rating{
        text-align: center;
    }
    .laptop-card >p{
        text-align: center;
    }

    .laptop-card .hot-sale{
        background-color: red;
        color: white;
        padding: 3px 13px;
    }
    .laptop-card > p{
        padding: 30px 0 20px 0;
    
    }
    .price-tag{
        margin-left: 15px;
        color:#828588;
        text-decoration: line-through;
    
    }
    .laptop-card .fas{
        margin-top: 20px;
        color: gold;
    }
    .actual-price{
        color: red;
    }

    .card-sales{
        margin: 50px 0;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-column-gap: 30px;
    }

    @media only screen and (max-width: 767px) {
        .card-sales{
            margin: 50px 0;
            display: grid;
            justify-content: center;
            grid-template-columns: 1fr;
            grid-column-gap: 30px;
        }
    }
    
`