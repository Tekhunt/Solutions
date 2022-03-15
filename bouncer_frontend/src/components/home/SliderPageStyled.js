import styled from 'styled-components';

export const SliderWrapper = styled.div`
    background-image:linear-gradient(63deg, #ff4858 -25%, #8f65ff 118%);
   .slides {
    width: 100%;
    height: 600px;
   }

    .slides .slick-prev,
    .slide .slick-next {
        position: absolute;
        top: 50%;
        z-index: 1,
    }
    .slides .slick-prev {
        /* border: 3px solid red; */
        left: 5%;
    }
    .slides .slick-next {
        right: 10%;
        /* background-color: red; */
    }
    .slides-display {
        display: flex;
    }

    .slides .slides-carousel{
       display: flex;
       gap: 50px;
       justify-content: space-between;
    }
    .slides .slides-carousel img{
        object-fit: contain;
        max-width: 100%;
        height: 600px;
        transform: translateY(-250px);
    }
   
    .slides .slide-heading{
        color: #fff;
        padding-left: 100px;
        transform: translateY(150px);
        width: 500px;
    }
    .slides .slide-heading > h2{
        margin: 40px 0;
        font-size: 2.25rem;
        font-weight: 600;
    }
    .slides .slide-heading > p{
        margin: 40px 0;
        font-size: 14px;
        font-weight: 300;
    }
    .slides .slide-heading > a{
       text-decoration: none;
       color:white;
       border-bottom: 3px solid white;
    }

    @media only screen and (max-width: 767px){
     
        .slides .slide-heading{
            color: #fff;
            padding-left: 50px;
            transform: translateY(150px);
            width: 500px;
    }
        .slides .slide-heading > h2{
            margin: 20px 0;
            font-size: 2.25rem;
            font-weight: 600;
    }
        .slides .slide-heading > p{
            margin: 20px 0;
            font-size: 14px;
            font-weight: 300;
    }
        .slides .slides-carousel img{
            object-fit: contain;
            max-width: 100%;
            height: 600px;
            transform: translateY(-70px);
            transform: translateX(50%);

    }
        
    }

`

export const DisplayWrapper = styled.div`
    display: flex;
    justify-content: space-between;
`