function MainLoader() {
  return (
    <div className="bg-zinc-200 h-screen w-screen p-0 m-0" >
      <div  className="text-3xl font-semibold flex items-center justify-center p-4">
        NGSpurs Object Detection
      </div>
      <div className="flex items-center justify-center gap-5">
      <img
        src="http://127.0.0.1:5000/video"
        alt="Live Video Stream"
        style={{ width: "600px", height: "440px" }}
        className="rounded-lg"
      />
      <img
        src="http://127.0.0.1:5000/video_detect"
        alt="Live Video Stream"
        style={{ width: "600px", height: "440px" }}
        className="rounded-lg"
      />
      </div>
      {/* <Login/> */}
    </div>
  );
}

export default MainLoader;
