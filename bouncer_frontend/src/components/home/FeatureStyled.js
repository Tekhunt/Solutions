import styled from 'styled-components';

export const FeatureWrapper = styled.section`
    .container-new{
        max-width: 1200px;
        margin: 50px auto;
        padding: 0 2rem;
        }
    .container-new > p{
        font-size: 2.0rem;
        margin: 30px 0;
        text-align: center;
        font-weight: 400;
    }
    .featured-products{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-column-gap: 50px;
    }
    .news-box{
        display: flex;
        justify-content: space-between;
        gap: 20px;
        margin: 20px 0;
    }
    .news-box .image-new{
        max-width: 100%;
        margin: 0 auto;
    }
    .news-box .news-text{
        max-width: 100%;
        margin: 0 auto;
    }
    .news-box .news-date{
        color:#b4b5b6;
        /* text-align: center; */
        padding-top:20px;
    }

    .news-box div > h4{
        margin: 20px 0;
        /* text-align: center; */
    }
    .container-new > h1{
        font-size: 2rem;
        margin: 50px 0;
        text-align: center;
        font-weight: 400;
    }
    .featured-sub{
        display: flex;
        justify-content: space-between;
        gap: 20px;
        margin: 30px 0;
    
    }
    .featured-sub div >img{
        border: 3px solid #F6F7F8;
        height: 150px;
        width: 150px;
    }
    .fas{
        margin: 10px 0;
        color: gold;
    }
    .price-tag{
        margin-left: 15px;
        color:#828588;
        text-decoration: line-through;
    
    }
   
    .actual-price{
        color: red;
    }

    .featured-sub > div:nth-child(2) p{
        margin-top: 10px;
    }

    @media only screen and (max-width: 767px) {
        .container-new > h1{
            font-size: 28px;
            margin: 30px 0;
            text-align: center;
            font-weight: 400;
        }
        .featured-products{
            display: grid;
            grid-template-columns: 1fr;
            justify-content: center;
            margin: 20px 0;
        }
        .featured-sub > div:nth-child(2) p{
            font-size: 14px;
        }
    }
   
`