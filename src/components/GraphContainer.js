import React from 'react';
import PropTypes from 'prop-types';
import SelectView from './SelectView';

const graphContainer = (GraphComponent, TableComponent, selector) => {
  class WrapperComponent extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        maxDomain: selector.getMaxField(
          this.props.data,
          this.props.groupBy,
          this.props.field,
          this.props.category
        ),
        filter: this.props.filter,
        view: this.props.view
      };

      this.updateSelect = this.updateSelect.bind(this);
      this.showSelectedComponent = this.showSelectedComponent.bind(this);
    }

    updateSelect(selected, name) {
      const setState = this.setState.bind(this);
      const { options, title } = this.state[name];

      setState({[name]: { options, selected, title }})
    }

    showSelectedComponent() {
      const { maxDomain, view } = this.state;
      const { data, ...props} = this.props;

      const selectedData = selector.selectData(
        data,
        this.props.groupBy,
        this.props.field,
        this.props.category,
        this.state.filter
      )

      if (view.selected === 'graph') {
        return (
          <GraphComponent
            data={selectedData}
            maxDomain={this.state.maxDomain}
            {...props}
          />
        );
      }
      else {
        return (
          <TableComponent
            data={selectedData}
            maxDomain={this.state.maxDomain}
            {...props}
          />
        );
      }
    }

    render() {

      const showSelectedComponent = this.showSelectedComponent;

      return (
        <div className="ds-l-col--12">
          <div className="ds-l-row ds-u-justify-content--end">
            <SelectView
              {...this.state.view}
              name={'view'}
              setState={this.updateSelect}
            />
            <SelectView
              {...this.state.filter}
              name={'filter'}
              setState={this.updateSelect}
            />
          </div>
          <div className="ds-l-row">
            {showSelectedComponent()}
          </div>
        </div>
      );
    }
  }

  WrapperComponent.propTypes = {
    data: PropTypes.array.isRequired,
    filter: PropTypes.object.isRequired,
    groupBy: PropTypes.string.isRequired,
    category: PropTypes.string.isRequired,
    field: PropTypes.string.isRequired,
    view: PropTypes.object.isRequired
  }

  return WrapperComponent
}

export default graphContainer;
