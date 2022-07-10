import React, {useEffect} from 'react';
import {Card, Col, Row, Divider, Image, Tag, Tabs, Typography, Skeleton, Avatar, Empty} from "antd";
import {Link} from "react-router-dom";
import removeLastCharacter from "../../utils/removeLastCharacter";
import BangumiScoreTag from "../BangumiScoreTag";
import InfoTimeline from "../InfoTimeline";
import CommentTimeLine from "../CommentTimeLine";
import Meta from "antd/es/card/Meta";
import Tags from "../Tags";
import axios from "axios";

const {TabPane} = Tabs

function GameInfo(props) {
    const {mobile,data} = props
    const keys = Object.keys(data.extra_data)
    return (
        <div>
            <div id={'result-container-bg'} style={{ background:`url("${removeLastCharacter(data.visuals)}")`}}/>
            <Card style={{margin:'2rem', minHeight:'45rem'}} id={'game-card'}>
                <Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }}>
                    <Row span={8}>
                        <div style={{display:'flex', flexDirection:'row'}}>
                        <div style={{margin:'1rem', display:'flex', justifyContent:'center'}}>
                                        <Image src={removeLastCharacter(data.visuals)}
                                               style={{borderRadius:'10px', minWidth:'10rem',minHeight:'15rem'}}
                                               placeholder = {
                                                   <Skeleton.Image active={true} style={{width:'10rem', height:'15rem'}}/>
                                               }
                                        />
                                    </div>
                            <Row style={{margin:'5px'}} span={6} gutter={{lg: 64}}>
                                <Col style={{marginBottom:'15px'}}>
                                    <div style={{fontSize:'20px', marginBottom:'20px'}} orientation={'left'}> · 游戏名</div>
                                    <div>
                                        <Tag style={{marginBottom:'.5rem'}}>中文名</Tag>
                                        {data.zh_name}<br/>
                                        <Tag style={{marginBottom:'.5rem'}}>原名</Tag>
                                        {data.primary_name}<br/>
                                        <Tag>别名</Tag>
                                        {
                                            data.names.map((item,index)=>{
                                                if(index===0){
                                                    return <span>{item}</span>
                                                }else{
                                                    return <span>、{item}</span>
                                                }
                                            })
                                        }
                                    </div>
                                </Col>
                                <Col style={{marginBottom:'15px'}}>
                                    <div style={{fontSize:'20px', marginBottom:'20px'}} orientation={'left'}> · 基本信息</div>
                                    {
                                        data.genre===undefined?'':
                                            data.genre===null?'':
                                                <div>
                                                    <Tag style={{marginBottom:'.5rem'}}>游戏类型</Tag>
                                                    {data.genre}
                                                </div>
                                    }
                                    {
                                        <div style={{display:'flex',alignItems:'center'}}>
                                            <Tag style={{marginBottom:'.5rem'}}>游戏评分</Tag>
                                            <BangumiScoreTag score={data.score_general} user_count={data.vote_count}
                                                            style={{fontSize:'0.7rem',marginBottom:'.5rem', padding:'0.1rem',width:'2.9rem',height:'1.3rem'}}
                                                            logoStyle={{width:'.8rem'}}/>
                                        </div>
                                    }
                                    {
                                        data.start_date===undefined?'':
                                            data.start_date===null?'':
                                                <div>
                                                    <Tag style={{marginBottom:'.5rem'}}>发售日期</Tag>
                                                    {data.start_date}
                                                </div>
                                    }
                                    {
                                        data.platform===undefined?'':
                                            data.platform===null?'':
                                                <div>
                                                    <Tag style={{marginBottom:'.5rem'}}>发售平台</Tag>
                                                    {data.platform.map((item,index)=>{
                                                        if(index===0){
                                                            return <span>{item}</span>
                                                        }else{
                                                            return <span>、{item}</span>
                                                        }
                                                    })}
                                                </div>
                                    }
                                    {
                                        data.engine===undefined?'':
                                            data.engine===null?'':
                                                <div>
                                                    <Tag style={{marginBottom:'.5rem'}}>游戏引擎</Tag>
                                                    {data.engine}
                                                </div>
                                    }
                                </Col>
                                <Col style={{marginBottom:'15px'}}>
                                    {data.extra_data===undefined?'':
                                        data.extra_data===null?'':
                                            <div>
                                                <div style={{fontSize:'20px', marginBottom:'20px'}} orientation={'left'}> · 其他信息</div>
                                                {
                                                    keys.map((item, index)=>{
                                                        return(
                                                            <div style={{whiteSpace: 'nowrap',
                                                                width: '100%',
                                                                overflow: 'hidden',
                                                                textOverflow:'ellipsis'}}>
                                                                <Tag style={{marginBottom:'.5rem'}}>{item}</Tag>
                                                                {item === "官方网站" ? <a href={data.extra_data[item]}>{data.extra_data[item]}</a>: data.extra_data[item]}
                                                            </div>
                                                        )
                                                    })
                                                }
                                            </div>
                                    }
                                </Col>
                            </Row>
                        </div>
                    </Row>
                    <Row span={17}>
                        <Tabs defaultActiveKey="1"  onChange={() => {
                            setTimeout(() => {
                                const relevantContainer = document.getElementById('relevant-container');
                                let resultContainer = document.getElementById('result-container');
                                relevantContainer.style.top = resultContainer.offsetHeight + 'px'
                                const container = document.getElementById('detail-container');
                                container.style.height = document.body.scrollHeight.toString() + 'px';
                            }, 200)
                        }}>
                            <TabPane key={'1'} tab={"游戏简介"}>
                                <div style={{display:'flex',flexDirection:'column',padding:'1rem 1rem 0 1rem'}}>
                                    <Typography.Paragraph><InfoTimeline descriptionArray={data.description.split('<br>')}/></Typography.Paragraph>
                                    <Typography.Title level={5}>{data.zh_name}的常见标签：</Typography.Title>
                                    <div style={{width:`${mobile ? '100%':'60%'}`, margin:'2rem auto 2rem auto'}}>
                                        <Tags tags={data.tags} history={props.history}/>
                                    </div>
                                </div>
                            </TabPane>
                            <TabPane tab="主要角色" key="2" style={{borderRadius:'10px'}}>
                                <div style={{display:'flex', flexWrap:'wrap', justifyContent:'center', alignContent:'center', marginTop:'2rem'}}>
                                    {
                                        data.chara_list.map(item =>
                                            (
                                                <Card hoverable style={{marginBottom:'1rem', marginRight:'1rem'}}>
                                                    <Meta
                                                        avatar={
                                                            <Avatar src={item.visuals} draggable/>
                                                        }
                                                        style={{minWidth:'15rem', marginRight:'2rem'}}
                                                        title={<Link>{item.primary_name}</Link>}
                                                        description={<div>
                                                            中文名：{item.zh_name}<br/>声优：{item.cv}
                                                        </div>}
                                                    />
                                                </Card>
                                            )
                                        )
                                    }
                                    {
                                        data.chara_list.length === 0 ? <Empty style={{marginTop:'4rem'}} image={Empty.PRESENTED_IMAGE_SIMPLE} description={'暂无角色介绍'}/>:''
                                    }
                                </div>
                            </TabPane>
                            <TabPane tab="评述讨论" key="3" style={{paddingLeft:'1rem', maxHeight:'60rem', overflowY:'scroll', overflowX:'hidden'}}>
                                <CommentTimeLine comments={data.comment_box}/>
                            </TabPane>
                        </Tabs>
                    </Row>
                </Row>
            </Card>
        </div>
    );
}

export default GameInfo;