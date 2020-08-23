import React, { useCallback, useState, useEffect } from 'react';
import { PlaidLink } from 'react-plaid-link';
import axios from "axios";
import Loading from "./Loading";
import Button from "@material-ui/core/Button";

const Transactions = () => {
    const [publicTokenG, setPublicTokenG] = useState("");
    const [linkToken, setLinkToken] = useState("");
    const onSuccess = useCallback((token, metadata) => {
        axios.post("/api/set_access_token", { public_token: token });
        setPublicTokenG(token);
    }, []);
        
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

