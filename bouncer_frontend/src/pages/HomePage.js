import React from 'react'
import CarouselSection from '../components/home/CarouselSection'
import Delivery from '../components/home/Delivery'
import DisplayProduct from '../components/home/DisplayProduct'
import Features from '../components/home/Features'
import Footer from '../components/home/Footer'
import Logo from '../components/home/Logo'
import NavBarPage from '../components/home/NavBar'
import NavItem from '../components/home/NavItem'
import News from '../components/home/News'
import Product from '../components/home/Product'
import SearchForm from '../components/home/SearchForm'
import Slider from '../components/home/SliderPage'
import TopFooter from '../components/home/TopFooter'
import TopNav from '../components/home/TopNav'


function HomePage() {

    return (
        <div>
            <TopNav />
            < Logo />
            < NavBarPage />
            <Slider />
            < CarouselSection />
            <NavItem />
            <Product />
            <DisplayProduct />
            <Delivery />
            <News/>
            <Features />
            <SearchForm />
            < hr />
            <TopFooter />
            <hr />
            <Footer />
        </div>
    )
}

export default HomePage

