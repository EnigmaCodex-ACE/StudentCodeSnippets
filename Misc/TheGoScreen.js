import React, {Component} from 'react';
import {
  Text,
  View,
  StyleSheet,
  Image,
  ScrollView,
  FlatList,
  TouchableOpacity,
  ImageBackground,
} from 'react-native';
import {
  createDrawerNavigator,
  createAppContainer,
  createBottomTabNavigator,
} from 'react-navigation';
import Icon from 'react-native-vector-icons/Ionicons';
import Icon1 from 'react-native-vector-icons/Entypo';
import Add from './Add.js';
import ProfileScreen from './Profile.js';
type Props = {};
export default class Pagego extends Component<Props> {
  constructor(props) {
    super(props);
    this.state = {loaded: false};
  }
  static navigationOptions = {
    header: null,
  };
  render() {
    return (
      <View style={styles.container}>
        <ImageBackground
          source={{
            uri:
              'data:image/jpeg;base64,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',
          }}
          style={{width: '100%', height: '100%'}}>
          <View style={styles.topBar}>
            <Icon name="ios-search" size={30} color="black" />
            <Text
              style={{
                fontSize: 20,
                borderWidth: 2,
                borderRadius: 5,
                width: '70%',
                textAlign: 'center',
                fontWeight: 'bold',
                backgroundColor: 'white',
              }}>
              Search for people or exciting places
            </Text>
            <TouchableOpacity
              onPress={() => {
                this.props.navigation.openDrawer();
              }}>
              <Icon1 name="menu" size={30} color="black" />
            </TouchableOpacity>
          </View>
          <View style={styles.most}>
            <Text style={{fontSize: 23, fontFamily: 'shadow'}}>
              Most Searched
            </Text>
            <View style={styles.searched}>
              <Text
                style={{
                  fontSize: 30,
                  borderWidth: 2,
                  borderRadius: 5,
                  width: '30%',
                  textAlign: 'center',
                  fontWeight: 'bold',
                  backgroundColor: 'white',
                }}>
                1
              </Text>
              <Text
                style={{
                  fontSize: 30,
                  borderWidth: 2,
                  borderRadius: 5,
                  width: '30%',
                  textAlign: 'center',
                  fontWeight: 'bold',
                  backgroundColor: 'white',
                }}>
                2
              </Text>
              <Text
                style={{
                  fontSize: 30,
                  borderWidth: 2,
                  borderRadius: 5,
                  width: '30%',
                  textAlign: 'center',
                  fontWeight: 'bold',
                  backgroundColor: 'white',
                }}>
                3
              </Text>
            </View>
          </View>

          <ScrollView style={styles.middle}>
            <Add
              x="Greece was wonderful"
              y="Bhavya Jain, traveller "
              z="Greece,Europe"
              k="Well, definitely not expected. I am a plus two student. I scored 178 marks by final frozen 
      ans key and I got a CRL 2651. Well I was blown off because everywhere, on 
      quora it was like marks vs rank will be according to 2016 model which 
      mean worst of worst I would have got 1600 rank. But the model matched 
      exactly with that of 2018, see now this is bullshit. So many loads of 
      bright and talented students in this session. This is why many have been 
      getting ranks around even double that of expectations. And this is competition, 
      you can't just complain that there are better students than you. So,anyways anybody should not curse and accuse himself/herself. 
      Luck factors and this year it was- Hardest students+ one of the 
      hardest paper."
            />
            <Add
              x="Check this place out"
              y="Bhavya Jain, travel guide"
              z="Rome,Italy"
              k="Well, definitely not expected. I am a plus two student. I scored 178 marks by final frozen 
      ans key and I got a CRL 2651. Well I was blown off because everywhere, on 
      quora it was like marks vs rank will be according to 2016 model which 
      mean worst of worst I would have got 1600 rank. But the model matched 
      exactly with that of 2018, see now this is bullshit. So many loads of 
      bright and talented students in this session. This is why many have been 
      getting ranks around even double that of expectations. And this is competition, 
      you can't just complain that there are better students than you. So,anyways anybody should not curse and accuse himself/herself. 
      Luck factors and this year it was- Hardest students+ one of the 
      hardest paper."
            />
          </ScrollView>
          <View style={styles.bottomBar}>
            <Text style={{fontSize: 23}}>Messages</Text>
            <Text style={{fontSize: 23}}>Uploads</Text>
            <Text style={{fontSize: 23}}>Notifications</Text>
          </View>
        </ImageBackground>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  topBar: {
    height: 30,
    justifyContent: 'space-around',
    flexDirection: 'row',
    marginTop: 7,
  },
  middle: {
    flex: 1,
    borderWidth: 2,
    borderRadius: 5,
    backgroundColor: 'white',
    marginTop: 7,
  },
  bottomBar: {
    flexDirection: 'row',
    height: 50,
    justifyContent: 'space-around',
    elevation: 20,
    backgroundColor: 'white',
  },
  most: {
    marginTop: 7,
  },
  searched: {
    justifyContent: 'space-around',
    flexDirection: 'row',
    marginTop: 7,
  },
});
