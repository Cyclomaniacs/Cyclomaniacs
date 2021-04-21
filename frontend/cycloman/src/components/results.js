import React from 'react';
import Loader from 'react-loader-spinner';
import axios from 'axios';
import {
    Card,
} from 'semantic-ui-react';
import {Link } from "react-router-dom";
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
    
    // componentDidMount() {
    //     // axios.defaults.headers.get['Access-Control-Allow-Origin'] = '*'
    //     let search_term = this.props.location.state
    //     search_term = search_term.split(' ');
    //     search_term = search_term.join('+');
    //     axios.get('http://localhost:5000/api/search?term=' + search_term)
    //     .then(res => {
    //         const items = res.data;
    //         console.log(items)
    //         this.setState( {items});
    //     })

    // }

        componentDidMount() {
        // axios.defaults.headers.get['Access-Control-Allow-Origin'] = '*'
        let search_term = this.props.location.state
        search_term = search_term.split(' ');
        search_term = search_term.join('+');

        this.setState({ loading: true }, () => {
            axios.get('http://localhost:5000/api/search?term=' + search_term)
                .then(results => this.setState( {
                    loading: false,
                    items: results.data
                }))

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

        const loading = this.state.loading
        console.log(loading)

        return (
            
            <div style={{textAlign: "center"}}>
                
                <div>
                <img src="logo4.PNG" class="centerImage" alt="Cyclomaniacs Logo" width="320" height="80"></img>
                </div>       
                <Button
                    color = 'black'
                    size = 'small'
                    href ="/"
                    >
                    Search Again
                </Button>
                <Button
                    color = 'black'
                    size = 'small'
                    href ="/aboutUs"
                    >
                    About Us
                </Button>
                <hr></hr>
                
                <div
                      style={{
                        width: "100%",
                        height: "100",
                        display: "flex",
                        justifyContent: "center",
                        alignItems: "center"
                      }}
                    >
                      {loading ? <Loader type="ThreeDots" color="#2BAD60" height="100" width="100" /> : <h2> </h2>}
                </div>

                <br></br>
                
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