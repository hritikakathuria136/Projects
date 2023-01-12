using UnityEngine;

public class MusicScript : MonoBehaviour
{
    AudioSource audioSource;

    void Awake()
    {
        float volume = PlayerPrefs.GetFloat("musicVolume");
        audioSource = GetComponent<AudioSource>();
        audioSource.volume = volume;
        audioSource.Play();
    }

}