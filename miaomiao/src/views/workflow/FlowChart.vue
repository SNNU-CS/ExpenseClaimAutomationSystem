<template>
  <v-card>
    <v-card-text>
      <v-chart :options="options"></v-chart>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      workflowId: this.$route.params.id,
      trans: [],
      states: [],
      defaultItemColor: "#33CC33",
      startItemStyle: {
        color: "blue" //开始
      },
      endItemStyle: {
        color: "red" //结束
      },
      options: {},
      defaultOptions: {
        title: {
          text: ""
        },
        tooltip: {},
        animationDurationUpdate: 1500,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            type: "graph",
            layout: "none",
            symbolSize: 50,
            roam: true,
            label: {
              show: true
            },
            edgeSymbol: ["circle", "arrow"],
            edgeSymbolSize: [4, 10],
            edgeLabel: {
              fontSize: 20
            },
            itemStyle: {
              color: "#33CC33" // 默认
            },
            lineStyle: {
              curveness: 0.5,
              color: "#000000",
              opacity: 0.8,
              width: 1
            },
            data: [],
            links: []
          }
        ]
      }
    };
  },
  mounted() {
    this.getTrans();
  },
  watch: {
    trans(result) {
      this.options = Object.assign({}, this.defaultOptions);
      let tempName = {};
      let tempOrder = {};
      // Todo: 处理子工作流的流程图
      for (let item of result) {
        // links
        let t = {
          source: item.source_state.name,
          target: item.destination_state.name,
          label: {
            show: true,
            formatter: item.attribute_type
          }
        };
        this.options.series[0].links.push(t);
        // data
        let tStateList = [item.source_state, item.destination_state];
        for (let state of tStateList) {
          if (tempName.hasOwnProperty(state.name) === false) {
            tempName[state.name] = "";
            if (tempOrder.hasOwnProperty(state.order) == false) {
              tempOrder[state.order] = 0;
            } else {
              tempOrder[state.order] += 1;
            }
            let tt = {
              name: state.name,
              x: 500 + tempOrder[state.order] * 300,
              y: state.order * 100
            };
            if (state.state_type === "初始状态") {
              tt["itemStyle"] = this.startItemStyle;
            } else if (state.state_type === "结束状态") {
              tt["itemStyle"] = this.endItemStyle;
            }
            this.options.series[0].data.push(tt);
          }
        }
      }
      this.options.title.text = this.trans[0].workflow + "的流程图";
    }
  },
  methods: {
    getTrans() {
      let self = this;
      this.$api.WorkflowTransitions(this.workflowId).then(function(response) {
        self.trans = response.result;
      });
    }
  }
};
</script>

<style></style>
