import React,{useState} from 'react';
import HelpLogo from '../../images/help.png'
import {Modal} from 'antd'
import './index.css'



function info() {
    Modal.info({
        title: <b>高级搜索指南</b>,
        content: (
            <div>
                <p>关键词求交</p>
                <p className="text">示例：<strong>宝可梦 AND 海贼王</strong></p>
                <p className="text">作用：优先返回“宝可梦”与“海贼王”均包含的结果</p>
                <p>关键词求并搜索</p>
                <p className="text">示例：<strong>宝可梦 OR 海贼王</strong></p>
                <p className="text">作用：优先返回“宝可梦”或“海贼王”的搜索结果</p>
                <p>关键词排除搜索</p>
                <p className="text">示例：<strong>柯南 NOT 少年侦探团</strong></p>
                <p className="text">作用：优先返回只有“柯南”但<strong>没有</strong>“少年侦探团”的搜索结果</p>
                <p>关键词模糊搜索</p>
                <p className="text">示例：<strong>cland~</strong></p>
                <p className="text">作用：忘记《Violet Evergarden》怎么拼？使用“vio~”进行模糊搜索吧！</p>
                <p className="text">提示：若依旧找不到，可在“~”后面添加数字进行更广的匹配。<strong>Vio~5</strong></p>
                <p className="text">注意：请使用小写字母</p>
            </div>
        ),
        onOk() {},
        width:600,
        centered:true,
        okText:'I get it!'
    });
}

function Help(props) {

    return (
        <div style={{position:'absolute',top:'2.1rem', right:'2.1rem', transform:'translate(50%,-50%)', cursor:'pointer'}}>
            <img style={{width:'1.5rem'}} src={HelpLogo} alt="帮助" onClick={info}/>
        </div>
    );
}

export default Help;