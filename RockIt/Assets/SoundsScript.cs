using UnityEngine;

public class SoundsScript : MonoBehaviour
{
    AudioSource audioSource;

    void Awake()
    {
        float volume = PlayerPrefs.GetFloat("soundsVolume");
        audioSource = GetComponent<AudioSource>();
        audioSource.volume = volume;
        audioSource.Play();
    }

}