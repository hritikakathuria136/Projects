using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class SettingsScreenSound : MonoBehaviour
{
    public Slider musicSlider;
    public Slider soundsSlider;

    void Awake()
    {
        musicSlider.value = PlayerPrefs.GetFloat("musicVolume");
        soundsSlider.value = PlayerPrefs.GetFloat("soundsVolume");
    }

    // Update is called once per frame

    void OnEnable()
    {
        musicSlider.onValueChanged.AddListener(delegate { changeMusicVolume(musicSlider.value); });
        soundsSlider.onValueChanged.AddListener(delegate { changeSoundsVolume(soundsSlider.value); });
    }

    //Called when Slider is moved
    void changeMusicVolume(float sliderValue)
    {
        PlayerPrefs.SetFloat("musicVolume", sliderValue);
        PlayerPrefs.Save();
    }
    void changeSoundsVolume(float sliderValue)
    {
        PlayerPrefs.SetFloat("soundsVolume", sliderValue);
        PlayerPrefs.Save();
    }

    void OnDisable()
    {
        //Un-Register Slider Events
        musicSlider.onValueChanged.RemoveAllListeners();
        soundsSlider.onValueChanged.RemoveAllListeners();
    }
}