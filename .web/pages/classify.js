import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, set_val, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, HStack, Image, Input, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, option, Select, SimpleGrid, Text, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import ReactDropzone from "react-dropzone"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])

  const [files, setFiles] = useState([]);

  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <Box>
  <VStack sx={{"padding": "5em"}}>
  <VStack>
  <Select onChange={(_e0) => addEvents([Event("state.upload_state.set_option", {value:_e0.target.value})], (_e0))} placeholder={`Select an example.`} sx={{"colorSchemes": "twitter"}}>
  {state.upload_state.options.map((wdtcwjnw, i) => (
  <option key={i} value={wdtcwjnw}>
  {wdtcwjnw}
</option>
))}
</Select>
</VStack>
  <ReactDropzone accept={{"application/pdf": [".pdf"], "image/png": [".png"], "image/jpeg": [".jpg", ".jpeg"], "image/gif": [".gif"], "image/webp": [".webp"], "text/html": [".html", ".htm"]}} disabled={false} maxFiles={1} multiple={false} onDrop={e => setFiles((files) => e)}>
  {({ getRootProps, getInputProps }) => (
    <Box sx={{"onKeyboard": true, "border": "1px dotted rgb(107,99,246)", "padding": "5em"}} {...getRootProps()}>
    <Input type={`file`} {...getInputProps()}/>
    <VStack>
    <Button sx={{"color": "rgb(107,99,246)", "bg": "white", "border": "1px solid rgb(107,99,246)"}}>
    {`Select File`}
  </Button>
    <Text>
    {`Drag and drop files here or click to select files`}
  </Text>
  </VStack>
  </Box>
  )}
</ReactDropzone>
  <HStack>
  <Button onClick={(_e) => addEvents([Event("state.upload_state.handle_upload", {files:files}, "uploadFiles")], (_e))}>
  {`Upload`}
</Button>
  <Button onClick={(_e) => addEvents([Event("state.upload_state.clear_files", {})], (_e))}>
  {`Clear`}
</Button>
  <Button onClick={(_e) => addEvents([Event("state.upload_state.predicte", {})], (_e))}>
  {`Submit`}
</Button>
</HStack>
  <HStack>
  {files.map((f) => f.name).map((bqnusjjq, i) => (
  <Text key={i}>
  {bqnusjjq}
</Text>
))}
</HStack>
  <SimpleGrid columns={[2]} spacing={`5px`} sx={{"align": "center"}}>
  {state.upload_state.img.map((bhpkslpk, i) => (
  <VStack key={i}>
  <Image src={bhpkslpk}/>
  <Text>
  {bhpkslpk}
</Text>
</VStack>
))}
</SimpleGrid>
</VStack>
</Box>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
