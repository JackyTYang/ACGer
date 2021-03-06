import React from 'react';
import Header from "../../components/Header";
import SearchBar from "../../components/SearchBar";
import HotWords from "../../components/HotWords";
import Help from "../../components/Help";
import './index.css'
import {Avatar, List} from "antd";

function Index (props) {
    return (
        <div id={'content'}>
            <div id="bg"/>
            <div id="top">
                <Help/>
                <Header/>
                <SearchBar history={props.history}/>
            </div>
            <HotWords history={props.history}/>
        </div>
    );
}

export default Index;