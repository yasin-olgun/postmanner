from burp import IBurpExtender,IBurpExtenderCallbacks,ITab,IHttpListener
from javax.swing import JPanel,JTable,JScrollPane,Box,BoxLayout,JCheckBox, JSplitPane,JLabel,SwingConstants,JTextField,JComboBox,ListSelectionModel,JButton,JFileChooser
from java.awt import BorderLayout, Dimension,Font
from javax.swing.table import DefaultTableModel
from javax import swing
from javax.swing.border import LineBorder
from java.awt import Color, BorderLayout, Dimension, Font, GridLayout, Insets

class Postmanner(ITab,IHttpListener):
    def __init__(self,extender):
        self.extender = extender

        self.tableModel = DefaultTableModel(["Index","Method","URL","MIME Type"],0)
        self.table = JTable(self.tableModel)
        self.requests_data = []

        
        self.init_ui()

    def getTabCaption(self):
        return "Postmanner"

    def init_ui(self):
        self.component = JPanel()

        self.component = JPanel(BorderLayout())
     
        # Create a panel for left space
        left_space_panel = JPanel()
        left_space_panel.setPreferredSize(Dimension(30, 0))  # Adjust width as needed

        # Create a panel for right space
        right_space_panel = JPanel()
        right_space_panel.setPreferredSize(Dimension(30, 0))  # Adjust width as needed

        # Create top panel
        top_panel = JPanel()
        top_panel.setLayout(None)
        # Add components to top panel as needed

        # Create bottom panel
        bottom_panel = JPanel()
        # Add components to bottom panel as needed

        # Create split pane to hold top and bottom panels
        split_pane = JSplitPane(JSplitPane.VERTICAL_SPLIT, top_panel,JScrollPane(self.table))
        #split_pane = JSplitPane(JSplitPane.VERTICAL_SPLIT, top_panel, JScrollPane(self.table))
        split_pane.setResizeWeight(0.2)



        title = JLabel("Postmanner");
        title.setBounds(10,10,100,30)
        labelFont = title.getFont()
        boldFont = Font(labelFont.getFontName(), Font.BOLD, 14)
        title.setFont(boldFont)

        
        labelCollectionName = JLabel("Collection Name: ")   
        inputCollectionName = JTextField(20)
        
        labelCollectionName.setBounds(10,50,500,30)     
        inputCollectionName.setBounds(110,50,400,30)

        items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

        labelDomain = JLabel("Domain List: ")
        domainList = JComboBox(items)
        domainList.setSelectedIndex(0)
        #domainList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION)


        labelDomain.setBounds(10,95,500,30)
        domainList.setBounds(110,95,400,30)

        saveButton = JButton("Save", actionPerformed=self.saveAction)
        saveButton.setBounds(110,130,75,25)

        titleFilter = JLabel("Method Filter");
        titleFilter.setBounds(570,10,100,30)
        labelFont = titleFilter.getFont()
        boldFont = Font(labelFont.getFontName(), Font.BOLD, 14)
        titleFilter.setFont(boldFont)

        allCheckBox = JCheckBox("ALL")
        allCheckBox.setBounds(570,42,50,30)

        getCheckBox = JCheckBox("GET")
        getCheckBox.setBounds(570,62,50,30)

        postCheckBox = JCheckBox("POST")
        postCheckBox.setBounds(570,82,50,30)

        putCheckBox = JCheckBox("PUT")
        putCheckBox.setBounds(570,102,50,30)

        deleteCheckBox = JCheckBox("DELETE")
        deleteCheckBox.setBounds(650,42,70,30)

        patchCheckBox = JCheckBox("PATCH")
        patchCheckBox.setBounds(650,62,70,30)

        optionsCheckBox = JCheckBox("OPTIONS")
        optionsCheckBox.setBounds(650,82,70,30)



        mimeTypes = ["HTML","JSON","Script","Text"]

        titleMimeType = JLabel("MIME Type Filter");
        titleMimeType.setBounds(770,10,150,30)
        labelFont = titleFilter.getFont()
        boldFont = Font(labelFont.getFontName(), Font.BOLD, 13)
        titleMimeType.setFont(boldFont)


        AllMimeTypeCheckBox = JCheckBox("ALL")
        AllMimeTypeCheckBox.setBounds(770,42,100,30)

        HTMLCheckBox = JCheckBox("HTML")
        HTMLCheckBox.setBounds(770,62,100,30)
        


        JSONCheckBox = JCheckBox("JSON")
        JSONCheckBox.setBounds(770,82,100,30)

        ScriptCheckBox = JCheckBox("Script")
        ScriptCheckBox.setBounds(770,102,100,30)


        top_panel.add(title)
        top_panel.add(labelCollectionName)
        top_panel.add(inputCollectionName)
        top_panel.add(labelDomain)
        top_panel.add(domainList)
        top_panel.add(saveButton)

        top_panel.add(titleFilter)
        top_panel.add(postCheckBox)
        top_panel.add(putCheckBox)
        top_panel.add(allCheckBox)
        top_panel.add(getCheckBox)
        top_panel.add(deleteCheckBox)
        top_panel.add(patchCheckBox)
        top_panel.add(optionsCheckBox)
        
        top_panel.add(titleMimeType)
        top_panel.add(HTMLCheckBox)
        top_panel.add(ScriptCheckBox)
        top_panel.add(AllMimeTypeCheckBox)
        top_panel.add(JSONCheckBox)

        #bottom_panel.add(JScrollPane(self.table),BorderLayout.CENTER)
      

        # Add components to main panel with BorderLayout constraints
        self.component.add(left_space_panel, BorderLayout.WEST)
        self.component.add(right_space_panel, BorderLayout.EAST)
        self.component.add(split_pane, BorderLayout.CENTER)



    def getUiComponent(self):
        return self.component

    def saveAction(self,event):
        file_chooser = JFileChooser()
        file_chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY)
        response = file_chooser.showSaveDialog(None)
        if response == JFileChooser.APPROVE_OPTION:
            selected_directory = file_chooser.getSelectedFile()
            if selected_directory:
                # Write selected item to JSON file in the selected directory
                file_path = selected_directory.getAbsolutePath()
                #with open(file_path, 'w') as json_file:
                 #   json.dump({"selected_item": selected_item}, json_file)

    def extract_request_body(self, request):
        # Extract the request body from the request bytes
        helpers = self.extender._helpers
        request_info = helpers.analyzeRequest(request)
        request_body_offset = request_info.getBodyOffset()
        request_body_bytes = request[request_body_offset:]
        request_body = helpers.bytesToString(request_body_bytes)
        return request_body  

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        """
        if toolFlag != self.extender._callbacks.TOOL_PROXY:
            return

        helpers = self.extender._helpers

        requestInfo = helpers.analyzeRequest(messageInfo)
        response = messageInfo.getResponse()
        mimeType = ""
        requestUrl = ""
        method = ""
        if response is not None:
            responseInfo = helpers.analyzeResponse(response)
            mimeType = responseInfo.getStatedMimeType()


        if messageIsRequest:

            requestUrl = requestInfo.getUrl()
            method = requestInfo.getMethod()
        
        print(requestUrl,method,mimeType)
        """

        if toolFlag != self.extender._callbacks.TOOL_PROXY:
            return
        
        mimeTypeArr = ["HTML","JSON"]
        
        request = messageInfo.getRequest()
        response = messageInfo.getResponse()
        helpers = self.extender._helpers
        requestInfo = helpers.analyzeRequest(messageInfo)
        mimeType = ""
        
        if response is not None:
            responseInfo = helpers.analyzeResponse(response)
            mimeType = responseInfo.getStatedMimeType()
        
        requestUrl = requestInfo.getUrl()
        method = requestInfo.getMethod()
        
        responseBody = helpers.bytesToString(response)
        requestBody = helpers.bytesToString(request)
        

        request = messageInfo.getRequest()
        request_body = self.extract_request_body(request)
        print("Request Body:", request_body)


        if messageIsRequest:
          
            pass
        else:
            self.tableModel.addRow([self.tableModel.getRowCount(),method, requestUrl,mimeType])
            self.requests_data.append({"Method": method, "URL": requestUrl,"Request":requestBody,"Response":responseBody})
            #self.tableModel.setValueAt(possibleVuln,self.tableModel.getRowCount()-1,4)
               
        


class BurpExtender(IBurpExtender, IBurpExtenderCallbacks):
   
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Postmanner")

        postmanner = Postmanner(self)

        callbacks.addSuiteTab(postmanner)
        callbacks.registerHttpListener(postmanner)




