import React, {Component} from 'react';
import {
  Text,
  View,
  StyleSheet,
  Image,
  ScrollView,
  FlatList,
} from 'react-native';
import {createAppContainer, createBottomTabNavigator} from 'react-navigation';
import {createStackNavigator} from 'react-navigation-stack';
import LoginScreen from './Login';
import SignUpScreen from './SignUp';
import TheGoScreen from './TheGoScreen';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {loaded: false};
  }
  render() {
    return (
      <View style={styles.container}>
        <LoginContainer />
      </View>
    );
  }
}

const RootStack = createStackNavigator(
  {
    Login: {screen: LoginScreen},
    SignUp: {screen: SignUpScreen},
    Go: {screen: TheGoScreen},
  },
  {
    initialRouteName: 'Login',
  },
);
const LoginContainer = createAppContainer(RootStack);
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
});
