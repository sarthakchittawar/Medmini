import React, { useEffect, useState } from 'react';
import { View, TextInput, Text, StyleSheet, Dimensions, ActivityIndicator } from 'react-native';
import * as Device from 'expo-device';
import axios from 'axios';
import AnimatedEllipsis from 'react-native-animated-ellipsis';

const TextInputComponent = () => {
  const [text, setText] = useState('');
  const [ansText, setAnsText] = useState('');
  const [waitFlag, setFlag] = useState(true);
  const [myRAM, changeRAM] = useState(0);

  const handleTextChange = (inputText) => {
    setText(inputText);
  };

  const handleTextSubmit = async () => {
    try {
      console.log(myRAM, text);
      const url = "http://10.2.133.59:5000/query";
      const headers = {
        'Content-Type': 'application/json',
      };

      const requestBody = {
        "question": text,
        "RAM": myRAM
      };

      setFlag(false);

      const response = await axios.post(url, requestBody, { headers });

      const posts = response.data;
      console.log('Fetched Answer:', posts);
      setAnsText(posts);
      setFlag(true);
    } catch (error) {
      setFlag(true);
      console.error('API Error:', error);
    }
  };

  useEffect(() => {
    changeRAM(Device.totalMemory);
  }, []);

  // useEffect(() => {
  //   setText("")
  // },[ansText])1

  const { width } = Dimensions.get('window');
  const inputWidth = 0.75 * width;

  return (
    <View style={styles.container}>
      <Text style={styles.medminiText}>MEDMINI</Text>
      <TextInput
        style={[styles.input, { width: inputWidth }]}
        onChangeText={handleTextChange}
        onEndEditing={handleTextSubmit}
        value={text}
        editable={waitFlag}
        placeholder="Type something..."
        returnKeyType="done"
      />
      {waitFlag ? (
        <Text style={[styles.text, { width: inputWidth }]}> {ansText}</Text>
      ) : (
        <View style={styles.loaderContainer}>
          {/* <ActivityIndicator size="large" color="#00FFFF" /> */}
          <AnimatedEllipsis numberOfDots={4} animationDelay={100} style= {{ color: "#00FFFF", fontSize: 25 }} />
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'black',
  },
  input: {
    height: 40,
    borderColor: '#00FFFF',
    borderWidth: 1,
    color: 'white',
    paddingLeft: 10,
    borderRadius: 15,
  },
  medminiText: {
    position: 'absolute',
    top: 50,
    right: 1,
    color: 'white',
    fontSize: 20,
    fontWeight: 'bold'
  },
  text: {
    paddingTop: 35,
    color: 'white',
    alignItems: 'center',
    justifyContent: 'center',
    textAlign: 'center'
  },
  loaderContainer: {
    paddingTop: 35,
    alignItems: 'center',
  },
});

export default TextInputComponent;