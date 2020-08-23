import React, { useCallback, useState, useEffect } from 'react';
import { PlaidLink } from 'react-plaid-link';
import axios from "axios";
import Loading from "./Loading";
import Button from "@material-ui/core/Button";

const Transactions = () => {
    const [publicTokenG, setPublicTokenG] = useState("");
    const [linkToken, setLinkToken] = useState("");
    const [transactions, setData] = useState({});
    const [showData, setShowData] = useState(false);
        
    useEffect(() => {
        async function fetchData(){    
            await fetch("/api/create_link_token", {method : "POST"})
            .then((response) => { 
                if (response.ok)  return response.json()
                else alert("Not ok!"); return;
            })
            .then(data => setLinkToken(data["link_token"]));

            await axios.post("/api/set_access_token", { public_token: linkToken });
            setPublicTokenG(linkToken);

            await fetch("/api/transactions", {method : "POST"}).then((response) => {
                if (response.ok)  return response.json()
                else alert("Not ok!"); return;
            })
            .then(data => setData(transactions));
        }
        fetchData();
    }, []);
    

    if (Object.keys(transactions).length > 0)
        return (
          <React.Fragment>
          <Button
            onClick = {() => setShowData(true)}
          >
            Get Data
          </Button>
          </React.Fragment>
        );

    return <Loading/>;
};
export default Transactions;

