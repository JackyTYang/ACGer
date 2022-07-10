import {
    Button,
    Card,
    Col,
    Image,
    Row,
    Typography,
    Skeleton,
    Tabs,
    Avatar,
    Divider,
    message,
    Empty, Tag
} from "antd";
import Meta from "antd/es/card/Meta";
import Tags from "../Tags";
import BiliBiliScoreTag from "../BiliBiliScoreTag";
import BangumiScoreTag from "../BangumiScoreTag";
import removeLastCharacter from "../../utils/removeLastCharacter";
import {PlayCircleOutlined} from "@ant-design/icons";
import CommentTimeLine from "../CommentTimeLine";
import InfoTimeline from "../InfoTimeline";
import InfoItem from "../InfoItem";
import {Link} from "react-router-dom";
import axios from "axios";
import React from "react";
const { TabPane } = Tabs;
function AnimeInfo (props) {
    const data = props.data;
    const mobile = props.mobile;
    const loading = props.loading;
    const bilibiliData = props.bilibiliData;
    const names = data.names;
    const zh_name = data.zh_name;
    const animation_company = data.animation_company;
    const made = data.made;
    const chara_list = data.chara_list;
    const director = data.director;
    const episode_count = data.episode_count;
    const music_composer = data.music_composer;
    const producer = data.producer;
    const comments = data.comment_box;
    const keys = Object.keys(data.extra_data);
    const generateRandomColor = () => {
        const r = Math.floor(Math.random()*200);
        const g = Math.floor(Math.random()*200);
        const b = Math.floor(Math.random()*200);
        return `rgba(${r}, ${g}, ${b}, 0.6)`;
    }
    const Score = () => <div style={{height:'1.5rem', width:'6rem', display:'flex', justifyContent:'space-between'}}>
        <BiliBiliScoreTag score={bilibiliData.media_score.score} user_count={bilibiliData.media_score.user_count}/>
        <BangumiScoreTag score={data.score_general} user_count={data.vote_count}/>
    </div>

    return (
        <div>
            <div id={'result-container-bg'} style={{ background:`url("${removeLastCharacter(data.visuals)}")`}}/>
            <Card style={{margin:'2rem', minHeight:'45rem'}} id={'anime-card'}>
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
                            <div style={{fontSize:'20px', marginBottom:'20px'}} orientation={'left'}> · 番剧名</div>
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
                                <div style={{display:'flex',alignItems:'center'}}>
                                    <Tag style={{marginBottom:'.5rem'}}>番剧评分</Tag><Score/>
                                </div>
                            }
                            {
                                data.start_date===undefined?'':
                                    data.start_date===null?'':
                                        <div>
                                            <Tag style={{marginBottom:'.5rem'}}>放送日期</Tag>
                                            {data.start_date}
                                        </div>
                            }
                            {
                                <div>
                                    <Tag style={{marginBottom:'.5rem'}}>话数</Tag>
                                    {episode_count}
                                </div>
                            }
                            {
                                <div>
                                    <Tag style={{marginBottom:'.5rem'}}>制作公司</Tag>
                                    {animation_company}
                                </div>
                            }
                            {
                                <div>
                                    <Tag style={{marginBottom:'.5rem'}}>导演</Tag>
                                    {director}
                                </div>
                            }
                        </Col>
                        <Col style={{marginBottom:'15px'}}>
                            <div style={{fontSize:'20px', marginBottom:'20px'}} orientation={'left'}> · 其他信息</div>
                            <div style={{display:'flex', marginBottom:'2rem', justifyContent:`space-around`}}>
                                {
                                    <div style={{display:'flex', justifyContent:`space-around`}}>
                                        <div style={{width:'45%'}}>
                                            {
                                                keys.slice(0, Math.floor(keys.length / 2)).map(item => (
                                                    <div style={{marginBottom:'.3rem'}}>
                                                        <Tag>{item}</Tag>
                                                        {
                                                            item === '官方网站' ? <a href={data.extra_data[item]}>{data.extra_data[item]}</a>:data.extra_data[item]
                                                        }
                                                    </div>
                                                ))
                                            }
                                        </div>
                                        <Divider type={'vertical'} style={{height:'100%'}}/>
                                        <div style={{width:'45%'}}>
                                            {
                                                keys.slice(Math.floor(keys.length / 2), keys.length).map(item => (
                                                    <div style={{marginBottom:'.3rem'}}>
                                                        <Tag>{item}</Tag>
                                                        {
                                                            item === '官方网站' ? <a href={data.extra_data[item]}>{data.extra_data[item]}</a>:data.extra_data[item]
                                                        }
                                                    </div>
                                                ))
                                            }
                                        </div>
                                    </div>
                                }
                            </div>
                        </Col>
                        </Row>
                        {bilibiliData.goto_url ?
                        <Button style={{backgroundColor:'#EA7A99', border:'0', display:'flex', alignItems:'center'}}
                                type={'primary'}
                                onClick={() => window.location.href=bilibiliData.goto_url}><PlayCircleOutlined />
                            B站播放</Button>:''}
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
                            <TabPane key={'1'} tab={"番剧简介"}>
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

export default AnimeInfo;