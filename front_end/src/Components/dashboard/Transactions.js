import React, { useCallback, useState, useEffect } from 'react';
import { PlaidLink } from 'react-plaid-link';
import Loading from "./Loading";
import Button from "@material-ui/core/Button";
import LogTable from "./TransactionComponents/LogTable";

const Transactions = (props) => {
    const [publicTokenG, setPublicTokenG] = useState("");
    const [linkToken, setLinkToken] = useState("");
    const [accessToken, setAccessToken] = useState("");
    const [itemID, setItemID] = useState(0);
    const [success, setSuccess] = useState(false);
    const [transactions, setData] = useState([]);

    // Link_Token
    useEffect(() => {
        async function fetchData(){    
            await fetch("/api/create_link_token", {method : "POST"})
            .then((response) => { 
                if (response.ok)  return response.json()
                else alert("Not ok!"); return;
            })
            .then(data => setLinkToken(data["link_token"]));
        }
        fetchData();
    }, []);
    
    // Access_Token
    const onSuccess = async function (token, metadata){
        await fetch("/api/set_access_token", {
            method: "POST",  
            headers: {"Content-Type": "application/json", "Accept" : "application/json", "mode": "no-cors"},
            body: JSON.stringify({'public_token': token})
        })
        setPublicTokenG(token);
        setSuccess(true);
    };
    
    // Get Transaction Data 
    useEffect(() => {
        if (!success) return;
        async function getTransactions(){
            await fetch("/api/transactions", {method : "GET"})
            .then((response) => {
                if (response.ok) return response.json()
                else alert("Not ok!"); return;
            }).then(data => { 
                props.fetchTransactions(data["transactions"])
                setData(data["transactions"]) 
            });
        }

        getTransactions();
    }, [success]);

    if (transactions && transactions.length > 0)
        return (<LogTable data={transactions}>
        </LogTable>);

    if (linkToken)
        return (
        <PlaidLink
            token={linkToken}
            onSuccess={onSuccess}
          >
            Connect to Your Bank Account 

        </PlaidLink>
        );
        

    return <Loading/>;
};
export default Transactions;

