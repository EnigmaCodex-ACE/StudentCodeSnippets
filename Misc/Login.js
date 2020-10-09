import React, {Component} from 'react';
import {
  Text,
  View,
  StyleSheet,
  Image,
  ScrollView,
  FlatList,
  ImageBackground,
} from 'react-native';

import Icon1 from 'react-native-vector-icons/Feather';

type Props = {};
export default class Login extends Component<Props> {
  render() {
    return (
      <View style={styles.container}>
        <ImageBackground
          source={{
            uri:
              'https://imgix.bustle.com/uploads/image/2018/4/13/0e213a84-847c-4266-9823-4706f197a7c1-fotolia_180853515_subscription_monthly_m.jpg?w=960&h=540&fit=crop&crop=faces&auto=format%2Ccompress&cs=srgb&q=70&dpr=2',
          }}
          style={{width: '100%', height: '100%'}}>
          <View style={styles.login}>
            <Text
              style={{
                fontSize: 30,
                borderWidth: 2,
                borderRadius: 5,
                width: '50%',
                textAlign: 'center',
                fontWeight: 'bold',
              }}
              onPress={() => {
                this.props.navigation.navigate('Login');
              }}>
              LOGIN
            </Text>
            <Text
              style={{
                fontSize: 30,
                borderWidth: 2,
                borderRadius: 5,
                width: '50%',
                textAlign: 'center',
                fontWeight: 'bold',
              }}
              onPress={() => {
                this.props.navigation.navigate('SignUp');
              }}>
              SIGNUP
            </Text>
          </View>
          <View style={styles.space}>
            <Icon1 name="aperture" size={90} color="blue" />
          </View>
          <View style={styles.box}>
            <Text
              style={{
                fontSize: 30,
                borderWidth: 2,
                borderRadius: 5,
                width: '75%',
                textAlign: 'center',
              }}>
              username
            </Text>
            <Text
              style={{
                fontSize: 30,
                borderWidth: 2,
                borderRadius: 5,
                width: '75%',
                textAlign: 'center',
              }}>
              password
            </Text>
          </View>
          <View style={styles.pass}>
            <Text style={{fontSize: 18}}>forgot password?</Text>
            <Text
              style={{
                fontSize: 30,
                borderWidth: 2,
                borderRadius: 5,
                width: '50%',
                textAlign: 'center',
                height: 50,
                fontWeight: 'bold',
              }}
              onPress={() => {
                this.props.navigation.navigate('TheGoScreen');
              }}>
              GO
            </Text>
          </View>
        </ImageBackground>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    width: '100%',
    backgroundColor: '#fff',
  },
  login: {
    flexDirection: 'row',
  },
  space: {
    height: '30%',
    justifyContent: 'center',
    marginLeft: 160,
  },
  box: {
    marginLeft: 100,
  },
  pass: {
    flex: 1,
    marginLeft: 150,
    flexDirection: 'column',
    marginTop: 25,
  },
});
