import React, {useState} from 'react';
import {useUpdate} from 'ahooks';
import {Collapse, List, Pagination, Tag, Typography} from "antd";
import {Link} from "react-router-dom";
import TypeTag from "../TypeTag";
import BangumiScoreTag from "../BangumiScoreTag";
import './index.css';
import removeLastCharacter from "../../utils/removeLastCharacter";

const { CheckableTag } = Tag;
const { Panel } = Collapse
const { Paragraph } = Typography
const tagsData = ['相关度','评论数', '最近', '评分'];

function BookShowList(props) {
    let filter = 'relate'
    const { total,currentPage,selectedTag } = props
    switch(selectedTag){
        case '相关度': filter = 'relate';break;
        case '评论数': filter = 'comment';break;
        case '最近': filter = 'recent';break;
        case '评分': filter = 'score';break;
    }
    const onChange = async (page,pageNum) => {
        sessionStorage.setItem('currentPage',page)
        await props.getData(page,filter,'book',pageNum)
        document.body.scrollTop = document.documentElement.scrollTop = 0;
    }

    const handleChange = async (tag,checked)=>{
        if(checked){
            switch(tag){
                case '相关度': filter = 'relate';break;
                case '评论数': filter = 'comment';break;
                case '最近': filter = 'recent';break;
                case '评分': filter = 'score';break;
            }
            sessionStorage.setItem('selectedTag',filter)
            await onChange(1,10)

        }
    }

    return (
        <div>
            {
                <div style={{marginLeft:'70%'}}>
                    {/*<Collapse ghost >*/}
                    {/*    <Panel header={'结果排序'} key={1} >*/}
                    {/*        {tagsData.map(tag => (*/}
                    {/*            <CheckableTag*/}
                    {/*                key={tag}*/}
                    {/*                checked={selectedTag===tag}*/}
                    {/*                onChange={checked => handleChange(tag, checked)}*/}
                    {/*            >*/}
                    {/*                {tag}*/}
                    {/*            </CheckableTag>*/}
                    {/*        ))}*/}
                    {/*    </Panel>*/}
                    {/*</Collapse>*/}
                    {tagsData.map(tag => (
                        <CheckableTag
                            key={tag}
                            checked={selectedTag===tag}
                            onChange={checked => handleChange(tag, checked)}
                        >
                            {tag}
                        </CheckableTag>
                    ))}
                </div>
            }
            {
                <List
                    itemLayout="vertical"
                    size="large"
                    dataSource={props.listData}
                    renderItem={item => (
                        <List.Item
                            key={item.guid}
                            extra={
                                <div style={{width:'10rem',height:'10rem',display:'flex',justifyContent:'center',alignItems:'center'}}>
                                    <Link to={{pathname:`/detailInfo/${item.guid}`}}>
                                        <img
                                            style={{width:'7rem'}}
                                            alt="logo"
                                            src={removeLastCharacter(item.image_urls)}
                                        />
                                    </Link>
                                </div>
                            }
                        >
                            <List.Item.Meta
                                title={<div style={{display:'flex',alignItems:'center',height:'2rem'}}>
                                    <TypeTag type={item.type}/>
                                    <Link to={{pathname:`/detailInfo/${item.guid}`}}
                                          style={{fontSize:'1.1rem',color:'black'}}
                                          dangerouslySetInnerHTML={item.zh_name}
                                    >
                                    </Link>&nbsp;&nbsp;
                                    {/*<h1 style={{fontSize:'0.8rem',color:'black',height:'2.3rem'}} > [原名]</h1>{<div style={{fontSize:'0.8rem',color:'black',height:'1.7rem'}} dangerouslySetInnerHTML={item.primary_name}/> || '暂无'}*/}
                                    {item.writer===null?'':
                                        item.writer.map((item,index)=>{
                                            if(index===0){
                                                return <span>{item}{'\u00A0\u00A0'}</span>
                                            }else{
                                                return <span>、{item}{'\u00A0\u00A0'}</span>
                                            }
                                        })
                                    }
                                    {item.press===null?'暂无':
                                        item.press.map((item,index)=>{
                                            if(index===0){
                                                return <span style={{fontSize:'0.8rem',color:'gray',height:'1.5rem'}}>{item}</span>
                                            }else{
                                                return <span style={{fontSize:'0.8rem',color:'gray',height:'1.5rem'}}>、{item}</span>
                                            }
                                        })
                                    }
                                    <h1 style={{fontSize:'0.8rem',color:'gray',height:'2.3rem'}}>{'\u00A0\u00A0'}{item.start_date || ''}</h1>
                                </div>}
                                description={
                                    item.tags===null?'':item.tags.map((item,index)=>{
                                        if(index<5){
                                            return <Tag><div dangerouslySetInnerHTML={item}/></Tag>
                                        }
                                    })}
                            />
                            {/*<div className={'item-info-tag'}><Tag color={'geekblue'}>原名</Tag>{<div dangerouslySetInnerHTML={item.primary_name}/> || '暂无'}</div>*/}
                            <div className={'item-info-tag'}>
                                <BangumiScoreTag
                                    score={item.score}
                                    user_count={item.vote_count}
                                    style={{fontSize:'0.7rem',padding:'0.1rem',width:'2.7rem',height:'1.2rem'}}
                                    logoStyle={{width:'.8rem'}}
                                />
                                <h1 style={{fontSize:'0.8rem',color:'black',height:'2.3rem'}}>({item.vote_count}人评价)</h1>
                            </div>
                            {/*<div className={'item-info-tag'}><Tag color={'geekblue'}>作者</Tag>*/}
                            {/*    {item.writer===null?'':*/}
                            {/*        item.writer.map((item,index)=>{*/}
                            {/*            if(index===0){*/}
                            {/*                return <span>{item}</span>*/}
                            {/*            }else{*/}
                            {/*                return <span>、{item}</span>*/}
                            {/*            }*/}
                            {/*        })*/}
                            {/*    }*/}
                            {/*</div>*/}
                            {/*<div className={'item-info-tag'}><Tag color={'geekblue'}>出版社</Tag>*/}
                            {/*    {item.press===null?'暂无':*/}
                            {/*        item.press.map((item,index)=>{*/}
                            {/*            if(index===0){*/}
                            {/*                return <span>{item}</span>*/}
                            {/*            }else{*/}
                            {/*                return <span>、{item}</span>*/}
                            {/*            }*/}
                            {/*        })*/}
                            {/*    }*/}
                            {/*</div>*/}
                            {/*<div className={'item-info-tag'}><Tag color={'geekblue'}>出版日期</Tag>{item.start_date || '暂无'}</div>*/}
                            <div className={'item-info-tag'}>
                                <div style={{color: "gray", fontSize:"11px",height:'auto',justifyContent:'center',alignItems:'center'}} id={'description-wrapper'} dangerouslySetInnerHTML={item.description}>
                                </div>
                            </div>
                        </List.Item>
                    )}
                />
            }
            {
                <div style={{float:'right'}}>
                    <Pagination showQuickJumper showSizeChanger={false} total={total} onChange={onChange} current={currentPage} defaultPageSize={10}/>
                </div>
            }
        </div>
    );
}

export default BookShowList;