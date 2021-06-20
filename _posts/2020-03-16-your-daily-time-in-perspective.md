---
title: Your time in perspective
date: 2020-03-14 05:52:03 +05:30
draft: True
categories:
- interactive
- general
layout: single
---

<div id="content"></div>


<script src="https://fb.me/react-15.1.0.min.js"></script>
<script src="https://fb.me/react-dom-15.1.0.min.js"></script>

<script type="text/javascript">

/*

// BABEL EXAMPLE: I can use react.useState to sync with the
// state and derive other state variables

class SimpleExample extends React.Component {
	// React components are simple functions that take in props and state, and render HTML
	render() {
		
	  let sleep_hours = 8;

      let sleep_blocks = sleep_hours * 6;

      let awake_hours = 24 - sleep_hours

      let awake_minutes = (awake_hours * 6 / 10) * 100

      let awake_10_min_blocks = awake_minutes / 10
		
	  return (
			<div> 
				You sleep about {sleep_hours} hours a night. That leaves {24 - sleep_hours} hours awake each day. Or about {awake_minutes} minutes. Let’s think about those {awake_minutes} minutes as {awake_10_min_blocks} 10-minute blocks. That’s what you wake up with every day.

Throughout the day, you spend 10 minutes of your life on each block, until you eventually run out of blocks and it’s time to go to sleep. Sometimes you overwork, which is to some extent, equivalent of borrowing blocks from the next day in advance.

So how are you using these {awake_10_min_blocks} blocks? 
			</div>
		);
	}
}

ReactDOM.render(<SimpleExample />, document.getElementById('content'));
*/

"use strict";

function _instanceof(left, right) { if (right != null && typeof Symbol !== "undefined" && right[Symbol.hasInstance]) { return !!right[Symbol.hasInstance](left); } else { return left instanceof right; } }

function _typeof(obj) { "@babel/helpers - typeof"; if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

function _classCallCheck(instance, Constructor) { if (!_instanceof(instance, Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } return _assertThisInitialized(self); }

function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }

function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); if (superClass) _setPrototypeOf(subClass, superClass); }

function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf || function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }

var SimpleExample = /*#__PURE__*/function (_React$Component) {
  _inherits(SimpleExample, _React$Component);

  function SimpleExample() {
    _classCallCheck(this, SimpleExample);

    return _possibleConstructorReturn(this, _getPrototypeOf(SimpleExample).apply(this, arguments));
  }

  _createClass(SimpleExample, [{
    key: "render",
    // React components are simple functions that take in props and state, and render HTML
    value: function render() {
      var sleep_hours = 8;
      var sleep_blocks = sleep_hours * 6;
      var awake_hours = 24 - sleep_hours;
      var awake_minutes = awake_hours * 6 / 10 * 100;
      var awake_10_min_blocks = awake_minutes / 10;
      return React.createElement("div", null, "You sleep about ", sleep_hours, " hours a night. That leaves ", 24 - sleep_hours, " hours awake each day. Or about ", awake_minutes, " minutes. Let\u2019s think about those ", awake_minutes, " minutes as ", awake_10_min_blocks, " 10-minute blocks. That\u2019s what you wake up with every day. Throughout the day, you spend 10 minutes of your life on each block, until you eventually run out of blocks and it\u2019s time to go to sleep. Sometimes you overwork, which is to some extent, equivalent of borrowing blocks from the next day in advance. So how are you using these ", awake_10_min_blocks, " blocks?");
    }
  }]);

  return SimpleExample;
}(React.Component);

ReactDOM.render(React.createElement(SimpleExample, null), document.getElementById('content'));	

</script>