import styled from 'styled-components';

export const NewWrapper = styled.section`
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
    .latest-news, .featured-products{
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
    .image-new{
        max-width: 100%;
        margin: 0 auto;
    }
    .news-text{
        max-width: 100%;
        margin: 0 auto;
    }
    .news-box .news-date{
        color:#b4b5b6;
        padding-top:20px;
    }

    .news-box div > h4{
        margin: 20px 0;
    }

    @media only screen and (max-width: 767px){
        .news-box{
            display: flex;
            justify-content: space-between;
            flex-direction: column;
        }
        .latest-news{
            display: grid;
            grid-template-columns: 1fr;
            justify-content: center;
            margin: 10px 0;
        }
        
        .news-box .image-new{
            max-width: 100%;
        }
        .news-box .news-text{
            text-align: center;
        }
        .news-box .news-date{
            color:#b4b5b6;
            padding-top:5px;
        }

        .news-box div > h4{
            margin: 10px 0;
        }
    }

`