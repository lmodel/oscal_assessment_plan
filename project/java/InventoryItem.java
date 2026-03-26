package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  A single managed inventory item within the system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InventoryItem  {

  private String uuid;
  private String description;
  private List<ImplementedComponent> implemented-components;
  private String remarks;
  private List<ResponsibleParty> responsible-parties;
  private List<Property> props;
  private List<Link> links;

}