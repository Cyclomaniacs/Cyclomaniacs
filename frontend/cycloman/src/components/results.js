import React from 'react';
import { useState } from 'react';
import { useEffect } from "react";
import { useLocation } from "react-router-dom";
import axios from 'axios';
import {
    Table,
    Card,
    Image,
    Label, 
	Grid,
	Header,
	Form,
	Segment,
	Button,
} from 'semantic-ui-react';

// function Results( {query}) {
    
//     return(
//         <div>
//         <h1>Please help me Im stuck in a washing machine</h1>
//         <h2>{query}</h2>
//         </div>
//     );
// }

class Results extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            items: []
        }
        
    }
    
    componentDidMount() {
        // axios.defaults.headers.get['Access-Control-Allow-Origin'] = '*'
        axios.get('http://localhost:5000/api/search?term=fox+ranger+gloves')
        .then(res => {
            const items = res.data;
            console.log(items)
            this.setState( {items});
        })

    }
    
    mycomp(a, b) {
        
        return parseFloat(a.price.replace(/[^0-9.-]+/g,"")) - parseFloat(b.price.replace(/[^0-9.-]+/g,""));
    }
    
    render() {
        // let sampledata = { "product": "Fox Ranger Gloves", "price": 40, "retailer": "Jenson USA", "link": "https://www.jensonusa.com/Fox-Ranger-Glove"}
        // let sampledata2 = { "product": "Small Hands", "price": 69, "retailer": "Jenson China", "link": "https://www.jensonusa.com/Fox-Ranger-Glove"}
        // console.log(this.props.location.state)
        // // console.log(this.state.items)
        // let samplearray = [sampledata, sampledata2]
        let samplearray = this.state.items
        samplearray = samplearray.sort(this.mycomp)
        
        console.log(samplearray)
        let myitems = []
        let colors = ['red', 'orange', 'blue', 'green', 'purple']
        for (var i = 0; i < samplearray.length; i++) {
            // console.log(samplearray[i].product)
            myitems.push(<Card
                fluid color = 'orange'
                href = {samplearray[i].link}
                header = {samplearray[i].name}
                meta = {samplearray[i].retailer}
                description= {samplearray[i].price} />)
        }

        return (
            <div>
                <h1> This is a test</h1>
                <h2>You Searched For : {this.props.location.state}</h2>
                <div name="CardList">
                    <Card.Group itemsPerRow={2}>

                        {myitems}

                    </Card.Group>
                </div>
            </div>
        )
    }
}

//you spelt default wrong lmao. I'm going to get taco bell brb
export default Results;