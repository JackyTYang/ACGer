import React, {useEffect} from 'react';
import {Card, Col, Skeleton, Divider, Row, Image, Tag, Tabs, Typography, Avatar, Empty} from "antd";
import {Link} from "react-router-dom";
import Tags from "../Tags";
import InfoTimeline from "../InfoTimeline";
import removeLastCharacter from "../../utils/removeLastCharacter";
import Meta from "antd/es/card/Meta";

const {TabPane} = Tabs

function BookInfo(props) {
    const {mobile, data} = props
    return (
        <div>
        <div id={'result-container-bg'} style={{ background:`url("${removeLastCharacter(data.visuals)}")`}}/>
        <Card style={{margin:'2rem 2rem 2rem 2rem', minHeight:'30rem'}} id={'book-card'}>
            <Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }} style={{display:'flex'}}>
                <Row span={6}>
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
                                <div style={{fontSize:'20px', marginBottom:'20px'}} orientation={'left'}> · 书籍名</div>
                                <div>
                                    <Tag style={{marginBottom:'.5rem'}}>中文名</Tag>{data.zh_name}<br/>
                                    <Tag style={{marginBottom:'.5rem'}}>原名</Tag>{data.primary_name}<br/>
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
                                <div>
                                    <Tag style={{marginBottom:'.5rem'}}>作者</Tag>
                                    {data.writer === null ? '暂无':data.writer.map((item,index) => {
                                    if(index===0){
                                            return <span key={index}>{item}</span>
                                    }else{
                                        return <span key={index}>、{item}</span>
                                    }
                                    })}<br/>
                                    <Tag style={{marginBottom:'.5rem'}}>出版社</Tag>
                                    {data.press.map((item,index) => {
                                    if(index===0){
                                            return <span key={index}>{item}</span>
                                    }else{
                                        return <span key={index}>、{item}</span>
                                    }
                                    })}<br/>
                                </div>
                            </Col>
                        </Row>
                    </div>
                </Row>
                <Row span={17}>
                    <Tabs defaultActiveKey="1" onChange={(key) => {
                        setTimeout(() => {
                            const relevantContainer = document.getElementById('relevant-container');
                            let resultContainer = document.getElementById('result-container');
                            relevantContainer.style.top = resultContainer.offsetHeight + 'px'
                            const container = document.getElementById('detail-container');
                            container.style.height = document.body.scrollHeight.toString() + 'px';
                        }, 200)
                    }}>
                        <TabPane key={'1'} tab={"书籍简介"}>
                            <div style={{display:'flex',flexDirection:'column',padding:'1rem'}}>
                                <Typography.Paragraph><InfoTimeline descriptionArray={data.description.split('<br>')}/></Typography.Paragraph>
                                <Typography.Title level={5}>{data.zh_name} 的常见标签：</Typography.Title>
                                <div style={{width:`${mobile ? '100%':'60%'}`, margin:'2rem auto 2rem auto'}}>
                                    <Tags tags={data.tags} history={props.history}/>
                                </div>
                            </div>
                        </TabPane>
                        <TabPane key="2" tab={"主要人物"}>
                            <div style={{marginTop:'2rem', display:'flex', justifyContent:'center', alignItems:'center', flexWrap:'wrap'}}>
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
                                                    中文名：{item.zh_name}
                                                </div>}
                                            />
                                        </Card>
                                    )
                                )
                            }
                                {
                                    data.chara_list.length === 0 ? <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} description={'暂无人物介绍'}/>:''
                                }
                            </div>
                        </TabPane>
                    </Tabs>
                </Row>
            </Row>
        </Card>
    </div>
    );
}

export default BookInfo;