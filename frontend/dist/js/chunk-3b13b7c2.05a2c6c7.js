(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3b13b7c2"],{"087e":function(e,t,n){"use strict";var i=n("53cb"),a=n.n(i);a.a},"53cb":function(e,t,n){},"9e79":function(e,t,n){"use strict";n.r(t);var i=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("page-view",[n("a-card",{style:{height:"100%"},attrs:{bordered:!1,bodyStyle:{padding:"16px 0",height:"100%"}}},[n("div",{staticClass:"account-settings-info-main",class:e.device},[n("div",{staticClass:"account-settings-info-left"},[n("a-menu",{style:{border:"0",width:"mobile"==e.device?"560px":"auto"},attrs:{mode:"mobile"==e.device?"horizontal":"inline",defaultSelectedKeys:["1"],selectedKeys:e.selectedKeys,type:"inner"},on:{openChange:e.onOpenChange}},[n("a-menu-item",{key:"/admin/faqs/english"},[n("router-link",{attrs:{to:{name:"FaqEnglish"}}},[e._v(" English ")])],1),n("a-menu-item",{key:"/admin/faqs/arabic"},[n("router-link",{attrs:{to:{name:"FaqArabic"}}},[e._v(" Arabic ")])],1)],1)],1),n("div",{staticClass:"account-settings-info-right"},[n("route-view")],1)])])],1)},a=[],s=(n("99af"),n("680a")),c=n("ac0d"),o={components:{RouteView:s["c"],PageView:s["b"]},mixins:[c["c"]],data:function(){return{mode:"inline",openKeys:[],selectedKeys:[]}},created:function(){this.updateMenu()},methods:{onOpenChange:function(e){this.openKeys=e},updateMenu:function(){var e=this.$route.matched.concat();this.selectedKeys=[e.pop().path]}},watch:{$route:function(e){this.updateMenu()}}},u=o,r=(n("087e"),n("2877")),d=Object(r["a"])(u,i,a,!1,null,"756b3e5b",null);t["default"]=d.exports}}]);