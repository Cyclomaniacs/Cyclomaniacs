import React from 'react';
import { useState } from 'react';
import { useEffect } from "react";
import { useLocation } from "react-router-dom";
import axios from 'axios';
import {
    Table,
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
    
    
    render() {
        // let sampledata = { "product": "Fox Ranger Gloves", "price": 40, "retailer": "Jenson USA", "link": "https://www.jensonusa.com/Fox-Ranger-Glove"}
        // let sampledata2 = { "product": "Small Hands", "price": 69, "retailer": "Jenson China", "link": "https://www.jensonusa.com/Fox-Ranger-Glove"}
        // console.log(this.props.location.state)
        // // console.log(this.state.items)
        // let samplearray = [sampledata, sampledata2]
        let samplearray = this.state.items
        let myitems = []
        for (var i = 0; i < samplearray.length; i++) {
            // console.log(samplearray[i].product)
            myitems.push(<Table.Row>
                <Table.Cell> { samplearray[i].name } </Table.Cell>
                <Table.Cell> { samplearray[i].price } </Table.Cell>
                {/* <Table.Cell> { samplearray[i].retailer } </Table.Cell> */}
                <Table.Cell> <a href= { samplearray[i].link }>Link</a> </Table.Cell>
            </Table.Row>)
        }

        return (
            <div>
                <h1> This is a test</h1>
                <h2>You Searched For : {this.props.location.state}</h2>
                <Table mytable>
                    <Table.Header>
                        <Table.Row>
                            <Table.HeaderCell>Product</Table.HeaderCell>
                            <Table.HeaderCell>Price</Table.HeaderCell>
                            {/* <Table.HeaderCell>Retailer</Table.HeaderCell> */}
                            <Table.HeaderCell>Link</Table.HeaderCell>
                        </Table.Row>
                    </Table.Header>

                    <Table.Body>
                        {myitems}
                        {/* for item in array:
                        <Table.Row>
                            <Table.Cell>
                                <Label ribbon>First</Label>
                            </Table.Cell>
                            <Table.Cell>Cell</Table.Cell>
                            <Table.Cell>Cell</Table.Cell>
                            <Table.Cell>Cell</Table.Cell>

                        </Table.Row>
                        <Table.Row>
                            <Table.Cell>
                                <Label ribbon>Second</Label>
                            </Table.Cell>
                            <Table.Cell>Cell</Table.Cell>
                            <Table.Cell>Cell</Table.Cell>
                            <Table.Cell>Cell</Table.Cell>

                        </Table.Row>

                        <Table.Row>
                            <Table.Cell>
                                <Label ribbon>Third</Label>
                            </Table.Cell>
                            <Table.Cell>Cell</Table.Cell>
                            <Table.Cell>Cell</Table.Cell>
                            <Table.Cell>Cell</Table.Cell>

                        </Table.Row> */}



                    </Table.Body>
                </Table>
            </div>
        )
    }
}

//you spelt default wrong lmao. I'm going to get taco bell brb
export default Results;